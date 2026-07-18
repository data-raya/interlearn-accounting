import streamlit as st

from database.database import (
    get_materi,
    get_user_progress,
    get_user_quiz
)

def quiz_page():

    st.title("📝 Daftar Quiz")

    materi = get_materi()

    progress = get_user_progress(
        st.session_state.user_id
    )

    hasil_quiz = get_user_quiz(
        st.session_state.user_id
    )

    materi_selesai = {
        item["ID Materi"]
        for item in progress
    }

    quiz_selesai = {
        item["ID Materi"]
        for item in hasil_quiz
    }

    for item in materi:

        st.markdown("<br>", unsafe_allow_html=True)

        col1, col2 = st.columns([4,1])

        with col1:

            st.subheader(item["Judul"])

            st.caption(item["Kategori"])

        with col2:

            if item["ID Materi"] in quiz_selesai:

                st.success("✅")

            elif item["ID Materi"] in materi_selesai:

                if st.button(
                    "Mulai",
                    key=item["ID Materi"]
                ):

                    st.session_state.id_materi = item["ID Materi"]

                    st.session_state.page = "quiz_detail"

                    st.rerun()

            else:

                st.button(
                    "🔒",
                    disabled=True,
                    key=f"kunci_{item['ID Materi']}"
                )

        st.divider()