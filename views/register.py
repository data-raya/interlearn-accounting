import streamlit as st
from database.database import register_user

def register_page():

    st.title("📝 Register")

    nama = st.text_input("Nama Lengkap")

    email = st.text_input("Email")

    password = st.text_input(
        "Password",
        type="password"
    )

    konfirmasi = st.text_input(
        "Konfirmasi Password",
        type="password"
    )

    if st.button(
        "Daftar",
        use_container_width=True
    ):

        if nama == "" or email == "" or password == "" or konfirmasi == "":

            st.warning("Semua data wajib diisi.")

        elif password != konfirmasi:

            st.error("Konfirmasi password tidak sama.")

        else:

            berhasil = register_user(
                nama,
                email,
                password
            )

            if berhasil:

                st.success("Akun berhasil dibuat.")

                st.session_state.page = "login"

                st.rerun()

            else:

                st.error("Email sudah terdaftar.")

    if st.button("⬅ Kembali ke Login"):

        st.session_state.page = "login"

        st.rerun()