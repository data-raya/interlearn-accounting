import streamlit as st


def sidebar():

    st.sidebar.image("assets/logo.png", width=90)

    st.sidebar.title("InterLearn")

    st.sidebar.caption("Media Pembelajaran Interaktif")

    st.sidebar.divider()

    st.sidebar.page_link(
        "app.py",
        label="Dashboard",
        icon="🏠"
    )

    st.sidebar.markdown("### 📚 Materi")

    st.sidebar.markdown("📘 Perpajakan")
    st.sidebar.markdown("📙 Akuntansi Manajemen")
    st.sidebar.markdown("📗 Akuntansi Keuangan Lanjutan")

    st.sidebar.divider()

    st.sidebar.page_link(
        "pages/quiz.py",
        label="Quiz",
        icon="📝"
    )

    st.sidebar.page_link(
        "pages/profil.py",
        label="Profil",
        icon="👤"
    )