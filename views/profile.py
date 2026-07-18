import streamlit as st

from database.database import (
    get_user_by_id,
    get_user_progress,
    get_user_quiz,
    get_rata_rata_quiz,
    get_materi
)


def profile_page():

    user = get_user_by_id(
        st.session_state.user_id
    )

    materi = get_materi()

    progress_user = get_user_progress(
        st.session_state.user_id
    )

    quiz_user = get_user_quiz(
        st.session_state.user_id
    )

    total_materi = len(materi)

    materi_selesai = len(progress_user)

    quiz_selesai = len(quiz_user)

    rata_rata = get_rata_rata_quiz(
        quiz_user
    )

    progress = (
        materi_selesai / total_materi * 100
        if total_materi > 0
        else 0
    )

    st.title("👤 Profile")

    st.divider()

    st.subheader("Informasi Akun")

    col1, col2 = st.columns(2)

    with col1:

        with st.container(border=True):
            st.caption("Nama")
            st.subheader(user["Nama"])

    with col2:

        with st.container(border=True):
            st.caption("Email")
            st.subheader(user["Email"])

    st.divider()

    st.subheader("Statistik Belajar")

    col1, col2 = st.columns(2)

    with col1:

        with st.container(border=True):
            st.caption("📖 Materi Selesai")
            st.subheader(f"{materi_selesai} / {total_materi}")

    with col2:

        with st.container(border=True):
            st.caption("📝 Quiz Selesai")
            st.subheader(f"{quiz_selesai} / {total_materi}")

    col3, col4 = st.columns(2)

    with col3:

        with st.container(border=True):
            st.caption("🏆 Nilai Rata-rata")

            if quiz_selesai == 0:
                st.subheader("-")
            else:
                st.subheader(f"{rata_rata}")

    with col4:

        with st.container(border=True):
            st.caption("📈 Progress")
            st.subheader(f"{progress:.0f}%")

    st.divider()

    if st.button(
        "🚪 Logout",
        use_container_width=True,
        type="primary"
    ):

        st.session_state.clear()

        st.rerun()