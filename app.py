import streamlit as st

from components.sidebar import sidebar
from views.home import home_page
from views.login import login_page

# ----------------------------
# Konfigurasi Halaman
# ----------------------------
st.set_page_config(
    page_title="InterLearn Accounting",
    page_icon="assets/logo.png",
    layout="wide",
    initial_sidebar_state="expanded"
)

def load_css():

    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False

    with open("styles/style.css") as f:

        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

load_css()

# ----------------------------
# Halaman Dashboard
# ----------------------------
# Jika belum login
if not st.session_state.logged_in:

    if "page" not in st.session_state:
        st.session_state.page = "login"

    if st.session_state.page == "login":

        login_page()

    elif st.session_state.page == "register":

        from views.register import register_page
        register_page()

# Jika sudah login
else:

    sidebar()

    if "page" not in st.session_state:
        st.session_state.page = "home"

    if st.session_state.page == "home":
        home_page()

    elif st.session_state.page == "chapter":
        from views.chapter import chapter_page
        chapter_page()

    elif st.session_state.page == "materi":
        from views.materi import materi_page
        materi_page()

    elif st.session_state.page == "quiz":
        from views.quiz import quiz_page
        quiz_page()

    elif st.session_state.page == "quiz_detail":
        from views.quiz_detail import quiz_page
        quiz_page()

    elif st.session_state.page == "hasil":
        from views.hasil import hasil_page
        hasil_page()

    elif st.session_state.page == "profile":
        from views.profile import profile_page
        profile_page()