import streamlit as st
from components.hero import hero
from components.course_card import course_card
from components.stat_card import stat_card

def home_page():

    # Hero Section
    hero()

    st.divider()

    # Progress
    st.subheader("📈 Progress Belajar")

    col1, col2 = st.columns([1, 3])

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

        stat_card(
            "📖",
            "Chapter Selesai",
            "0"
        )

    with col2:

        stat_card(
            "📝",
            "Quiz Selesai",
            "0"
        )

    with col3:

        stat_card(
            "🏆",
            "Nilai Rata-rata",
            "-"
        )

    # ============================
    # Kategori Materi
    # ============================

    st.subheader("📚 Kategori Materi")

    col1, col2, col3 = st.columns(3)

    with col1:

        course_card(
            icon="📘",
            title="Perpajakan",
            chapter="9 Chapter",
            description="Belajar PPh, PPN, dan pajak lainnya.",
            button_key="btn_pajak"
        )

    with col2:

        course_card(
            icon="📙",
            title="Akuntansi Manajemen",
            chapter="18 Chapter",
            description="Materi biaya, budgeting, pengambilan keputusan dan evaluasi kinerja.",
            button_key="btn_manajemen"
        )

    with col3:

        course_card(
            icon="📗",
            title="Akuntansi Keuangan Lanjutan",
            chapter="10 Chapter",
            description="Konsolidasi, investasi, transaksi antar perusahaan, dan lainnya.",
            button_key="btn_akl"
        )