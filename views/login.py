import streamlit as st

def login_page():

    st.title("🔐 Login")

    email = st.text_input("Email")

    password = st.text_input(
        "Password",
        type="password"
    )

    if st.button("Login"):

        st.write("Nanti kita sambungkan ke database")