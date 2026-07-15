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

# ----------------------------
# Sidebar
# ----------------------------
sidebar()

# ----------------------------
# Halaman Dashboard
# ----------------------------
home_page()