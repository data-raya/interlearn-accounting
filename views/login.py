import streamlit as st
from database.database import login_user

def login_page():

    st.title("🔐 Login")

    email = st.text_input("Email")

    password = st.text_input(
        "Password",
        type="password"
    )

    if st.button(
        "Login",
        use_container_width=True
    ):

        user = login_user(
            email,
            password
        )

        st.write(user)

        if user:

            st.session_state.logged_in = True
            st.session_state.user_id = user["ID User"]
            st.session_state.nama = user["Nama"]

            st.session_state.page = "home"

            st.rerun()

        else:

            st.error("Email atau Password salah.")

    st.divider()

    if st.button(
        "Belum punya akun? Register",
        use_container_width=True
    ):

        st.session_state.page = "register"

        st.rerun()