import streamlit as st

from components.hero import hero
from components.progress_circle import progress_circle
from components.course_card import course_card
from components.stat_card import stat_card
from database.database import (
    get_materi,
    get_user_progress,
    get_progress_kategori,
    get_user_quiz,
    get_rata_rata_quiz
)

from views import materi

def home_page():

    # Hero Section
    hero()

    st.divider()

    materi = get_materi()

    progress = get_user_progress(
        st.session_state.user_id
    )

    quiz = get_user_quiz(
        st.session_state.user_id
    )

    total_quiz = len(get_materi())

    quiz_selesai = len(quiz)

    rata_rata = get_rata_rata_quiz(
        quiz
    )

    total_chapter = len(materi)

    chapter_selesai = len(progress)

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
            stat_card(
            "📝",
            "Quiz",
            f"{quiz_selesai} / {total_quiz}"
        )

        st.markdown("")

        stat_card(
            "🏆",
            "Nilai Rata-rata",
            "-" if quiz_selesai == 0 else rata_rata
        )

    st.divider()

    # ==========================
    # Hitung Progress Kategori
    # ==========================

    selesai_pajak = get_progress_kategori(
        st.session_state.user_id,
        "Perpajakan"
    )

    progress_pajak = selesai_pajak / 12 * 100

    selesai_manajemen = get_progress_kategori(
        st.session_state.user_id,
        "Akuntansi Manajemen"
    )

    progress_manajemen = selesai_manajemen / 18 * 100

    selesai_akl = get_progress_kategori(
        st.session_state.user_id,
        "Akuntansi Keuangan Lanjutan"
    )

    progress_akl = selesai_akl / 10 * 100
        
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
            progress_pajak,
            "#FFE082",
            "btn_pajak",
            "Perpajakan"
        )

    with col2:

        course_card(
            "📊",
            "Akuntansi Manajemen",
            18,
            progress_manajemen,
            "#A5D6A7",
            "btn_manajemen",
            "Akuntansi Manajemen"
        )

    with col3:

        course_card(
            "📚",
            "Akuntansi Keuangan Lanjutan",
            10,
            progress_akl,
            "#90CAF9",
            "btn_akl",
            "Akuntansi Keuangan Lanjutan"
        )
    
    st.divider()