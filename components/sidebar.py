import streamlit as st


def sidebar():

    st.sidebar.image("assets/logo.png", width=90)

    st.sidebar.title("InterLearn")

    st.sidebar.caption("Media Pembelajaran Interaktif")

    st.sidebar.divider()

    if st.sidebar.button("🏠 Dashboard", use_container_width=True):
        st.session_state.page = "home"
        st.rerun()

    st.sidebar.markdown("### 📚 Materi")

    st.sidebar.markdown("📘 Perpajakan")
    st.sidebar.markdown("📙 Akuntansi Manajemen")
    st.sidebar.markdown("📗 Akuntansi Keuangan Lanjutan")

    st.sidebar.divider()

    if st.sidebar.button("📝 Quiz", use_container_width=True):
        st.session_state.page = "quiz"
        st.rerun()

    if st.sidebar.button("👤 Profil", use_container_width=True):
        st.session_state.page = "profil"
        st.rerun()