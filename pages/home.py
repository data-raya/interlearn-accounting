import streamlit as st
from components.hero import hero

def home_page():

    # Hero Section
    hero()

    st.divider()

    # Progress
    st.subheader("📈 Progress Belajar")

    col1, col2 = st.columns([1,3])

    with col1:
        st.metric(
            label="Progress",
            value="0%"
        )

    with col2:
        st.metric(
            label="Chapter",
            value="0 / 37"
        )

    st.divider()

    # Statistik
    st.subheader("📊 Statistik Belajar")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Chapter Selesai", 0)

    with col2:
        st.metric("Quiz Selesai", 0)

    with col3:
        st.metric("Nilai Rata-rata", "-")

    st.divider()

    # Kategori
    st.subheader("📚 Kategori Materi")

    col1, col2, col3 = st.columns(3)

    with col1:

        st.button(
            "Mulai Belajar",
            key="btn_pajak",
            use_container_width=True
        )

    with col2:

        st.button(
            "Mulai Belajar",
            key="btn_manajemen",
            use_container_width=True
        )

    with col3:

        st.button(
            "Mulai Belajar",
            key="btn_akl",
            use_container_width=True
        )