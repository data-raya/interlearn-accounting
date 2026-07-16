import os
import streamlit as st

from utils.pdf_utils import render_pdf_page, get_total_pages
from database.database import (
    get_materi_by_id,
    selesai_membaca
)

def materi_page():

    if "id_materi" not in st.session_state:

        st.warning("Materi tidak ditemukan.")
        return

    materi = get_materi_by_id(
        st.session_state.id_materi
    )

    if "slide" not in st.session_state:
        st.session_state.slide = 0

    st.title(materi["Judul"])

    st.caption(materi["Kategori"])

    st.divider()

    st.write(materi["Deskripsi"])

    st.info(f"📄 Jumlah Slide : {materi['Jumlah Slide']}")

    left, center, right = st.columns([1,4,1])

    with left:

        if st.button("⬅ Kembali"):

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

                st.stop()