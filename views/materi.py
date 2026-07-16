import os
import streamlit as st

from database.database import get_materi_by_id
from utils.pdf_utils import render_pdf_page, get_total_pages

def materi_page():

    if "id_materi" not in st.session_state:

        st.warning("Materi tidak ditemukan.")
        return

    materi = get_materi_by_id(
        st.session_state.id_materi
    )

    st.title(materi["Judul"])

    st.caption(materi["Kategori"])

    st.divider()

    st.write(materi["Deskripsi"])

    st.info(f"📄 Jumlah Slide : {materi['Jumlah Slide']}")

    col1, col2 = st.columns(2)

    with col1:

        if st.button("⬅ Kembali"):

            st.session_state.page = "chapter"
            st.rerun()

    with col2:

        if st.button(
            "🚀 Mulai Belajar",
            use_container_width=True
        ):

            pdf_path = os.path.join(
                "assets",
                "materi",
                materi["Nama File"]
            )

            image = render_pdf_page(
                pdf_path,
                0
            )

            st.image(
                image,
                use_container_width=True
            )