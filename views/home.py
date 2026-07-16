import streamlit as st

from components.hero import hero
from components.progress_circle import progress_circle
from components.course_card import course_card
from components.stat_card import stat_card
from database.database import get_materi
from views import materi

def home_page():

    # Hero Section
    hero()

    st.divider()

    materi = get_materi()

    total_chapter = len(materi)

    chapter_selesai = sum(
        1
        for item in materi
        if str(item["Selesai Membaca"]).upper() == "TRUE"
    )

    progress = (
        chapter_selesai / total_chapter * 100
        if total_chapter > 0
        else 0
    )

    # Progress
    st.subheader("📈 Progress Belajar")

    left, right = st.columns([1,2])

    with left:

        progress_circle(progress)

    with right:

        st.markdown("### Ringkasan")

        stat1, stat2 = st.columns(2)

        with stat1:
            stat_card(
            "📖",
            "Chapter",
            f"{chapter_selesai} / {total_chapter}"
            )

        with stat2:
            stat_card("📝", "Quiz", "0 / 40")

        st.markdown("")

        stat_card("🏆", "Nilai Rata-rata", "-")

    st.divider()

    # ============================
    # Kategori Materi
    # ============================

    st.subheader("📚 Kategori Materi")

    col1, col2, col3 = st.columns(3)

    with col1:

        course_card(
            "💰",
            "Perpajakan",
            12,
            0,
            "#FFE082",
            "btn_pajak",
            "Perpajakan"
        )

    with col2:

        course_card(
            "📊",
            "Akuntansi Manajemen",
            18,
            0,
            "#A5D6A7",
            "btn_manajemen",
            "Akuntansi Manajemen"
        )

    with col3:

        course_card(
            "📚",
            "Akuntansi Keuangan Lanjutan",
            10,
            0,
            "#90CAF9",
            "btn_akl",
            "Akuntansi Keuangan Lanjutan"
        )
    
    st.divider()