import os
import streamlit as st

from utils.pdf_utils import render_pdf_page, get_total_pages
from database.database import (
    get_materi_by_id,
    selesai_membaca,
    sudah_selesai_materi
)


def materi_page():

    # State ketika materi selesai
    if "materi_selesai" not in st.session_state:
        st.session_state.materi_selesai = False

    if "id_materi" not in st.session_state:

        st.warning("Materi tidak ditemukan.")
        return

    if (
        "materi_data" not in st.session_state
        or st.session_state.materi_data["ID Materi"] != st.session_state.id_materi
    ):

        st.session_state.materi_data = get_materi_by_id(
            st.session_state.id_materi
        )

    materi = st.session_state.materi_data

    if "status_materi" not in st.session_state:

        st.session_state.status_materi = sudah_selesai_materi(
            st.session_state.user_id,
            st.session_state.id_materi
        )

    sudah_selesai = st.session_state.status_materi

    if "slide" not in st.session_state:
        st.session_state.slide = 0

    st.title(materi["Judul"])

    st.caption(materi["Kategori"])

    st.divider()

    st.info(f"📄 Jumlah Slide : {materi['Jumlah Slide']}")

    left, center, right = st.columns([1,4,1])

    with left:

        if st.button("⬅ Kembali"):

            st.session_state.pop("materi_data", None)
            st.session_state.pop("status_materi", None)

            st.session_state.page = "chapter"
            st.session_state.slide = 0

            st.rerun()

    with center:

        pdf_path = os.path.join(
            "assets",
            "materi",
            materi["Nama File"]
        )

        total = get_total_pages(pdf_path)

        st.markdown(
            f"### Slide {st.session_state.slide+1} / {total}"
        )

        image = render_pdf_page(
            pdf_path,
            st.session_state.slide
        )

        st.image(
            image,
            use_container_width=True
        )

    col_prev, col_next = st.columns(2)

    with col_prev:

        if st.button(
            "⬅ Previous",
            disabled=st.session_state.slide == 0
        ):

            st.session_state.slide -= 1
            st.rerun()

    with col_next:

        if st.session_state.slide < total - 1:

            if st.button(
                "Next ➡",
                use_container_width=True
            ):

                st.session_state.slide += 1
                st.rerun()

        else:

            if st.button(
                "✅ Selesaikan Materi",
                use_container_width=True,
                type="primary"
            ):

                selesai_membaca(
                    st.session_state.user_id,
                    st.session_state.id_materi
                )

                st.session_state.materi_selesai = True
                st.session_state.status_materi = True

                st.rerun()

    # ==========================
    # Setelah materi selesai
    # ==========================

    if st.session_state.materi_selesai or sudah_selesai:

        st.success("✅ Materi sudah selesai dipelajari!")

        col1, col2 = st.columns(2)

        with col1:

            if st.button(
                "📝 Kerjakan Quiz",
                use_container_width=True
            ):

                st.session_state.materi_selesai = False
                st.session_state.slide = 0
                st.session_state.page = "quiz_detail"

                st.rerun()

        with col2:

            if st.button(
                "🏠 Dashboard",
                use_container_width=True
            ):

                st.session_state.pop("materi_data", None)
                st.session_state.pop("status_materi", None)

                st.session_state.materi_selesai = False
                st.session_state.slide = 0
                st.session_state.page = "home"

                st.rerun()