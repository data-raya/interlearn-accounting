import streamlit as st


def sidebar():

    st.sidebar.image(
        "assets/logo.png",
        width=90
    )

    st.sidebar.image(
        "assets/logo.png",
        width=170
    )

    st.sidebar.divider()

    # ======================
    # Dashboard
    # ======================

    if st.sidebar.button(
        "🏠 Dashboard",
        use_container_width=True
    ):

        st.session_state.page = "home"

        st.rerun()

    # ======================
    # Materi
    # ======================

    st.sidebar.subheader("📚 Kategori Materi")

    if st.sidebar.button(
        "📘 Perpajakan",
        use_container_width=True
    ):

        st.session_state.kategori = "Perpajakan"
        st.session_state.page = "chapter"

        st.rerun()

    if st.sidebar.button(
        "📙 Akuntansi Manajemen",
        use_container_width=True
    ):

        st.session_state.kategori = "Akuntansi Manajemen"
        st.session_state.page = "chapter"

        st.rerun()

    if st.sidebar.button(
        "📗 Akuntansi Keuangan Lanjutan",
        use_container_width=True
    ):

        st.session_state.kategori = "Akuntansi Keuangan Lanjutan"
        st.session_state.page = "chapter"

        st.rerun()

    st.sidebar.divider()

    # ======================
    # Quiz
    # ======================

    if st.sidebar.button(
        "📝 Quiz",
        use_container_width=True
    ):

        st.session_state.page = "quiz"

        st.rerun()

    # ======================
    # Profile
    # ======================

    if st.sidebar.button(
        "👤 Profile",
        use_container_width=True
    ):

        st.session_state.page = "profile"

        st.rerun()

    st.sidebar.divider()

    # ======================
    # Logout
    # ======================

    if st.sidebar.button(
        "🚪 Logout",
        use_container_width=True
    ):

        st.session_state.clear()

        st.session_state.logged_in = False
        st.session_state.page = "login"

        st.rerun()