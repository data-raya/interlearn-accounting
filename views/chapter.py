from database.database import get_materi_by_kategori
import streamlit as st

def chapter_page():

    st.title("📚 Daftar Chapter")
    
    kategori = st.session_state.get("kategori", "")

    st.caption(f"Kategori: {kategori}")

    materi = get_materi_by_kategori(kategori)

    if st.button("⬅ Kembali"):

        st.session_state.page = "home"
        st.rerun()

    st.divider()

    for item in materi:

        with st.container(border=True):

            col1,col2 = st.columns([6,1])

            with col1:

                st.subheader(item["Judul"])

                st.caption(item["Deskripsi"])

            with col2:

                if st.button(
                    "Buka",
                    key=item["ID Materi"]
                ):

                    st.session_state.id_materi = item["ID Materi"]
                    st.session_state.page="materi"
                    st.rerun()