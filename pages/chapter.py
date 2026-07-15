import streamlit as st

def chapter_page():

    st.title("📚 Daftar Chapter")

    if st.button("⬅ Kembali"):

        st.session_state.page = "home"
        st.rerun()

    st.divider()

    for i in range(1,10):

        with st.container(border=True):

            col1,col2 = st.columns([6,1])

            with col1:

                st.subheader(f"Chapter {i}")

                st.caption("Belum dipelajari")

            with col2:

                if st.button(
                    "Buka",
                    key=f"chapter{i}"
                ):

                    st.session_state.chapter = i
                    st.session_state.page="materi"
                    st.rerun()