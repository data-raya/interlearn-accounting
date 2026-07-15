import streamlit as st

from components.sidebar import sidebar
from pages.home import home_page

# ----------------------------
# Konfigurasi Halaman
# ----------------------------
st.set_page_config(
    page_title="InterLearn Accounting",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)

def load_css():

    with open("styles/style.css") as f:

        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

load_css()

# ----------------------------
# Sidebar
# ----------------------------
sidebar()

# ----------------------------
# Halaman Dashboard
# ----------------------------
home_page()