import streamlit as st
from database.database import login_user

def login_page():

    left, center, right = st.columns([2,1,2])

    with center:
        st.image(
            "assets/logo.png",
            width=140
        )

    st.markdown(
        """
        <h1 style="text-align:center; margin-bottom:0;">
        InterLearn 
        Accounting
        </h1>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <p style="text-align:center; opacity:0.7;">
            Silakan login untuk melanjutkan pembelajaran
        </p>
        """,
        unsafe_allow_html=True
    )

    st.write("")

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