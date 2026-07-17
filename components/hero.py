import streamlit as st

from database.database import get_user_by_id

def hero():

    user = get_user_by_id(
        st.session_state.user_id
    )
    
    left, right = st.columns([5, 1])

    with left:

        st.markdown(
            f"""
            <div class="card">

                <div class="main-title">
                    👋 Halo, {user["Nama"]}!
                </div>

                <div class="sub-title">

                    Belajar Akuntansi Lebih Mudah dan Interaktif

                    <br><br>

                    InterLearn Accounting menyediakan materi pembelajaran,
                    latihan soal, kuis, dan pemantauan progres belajar
                    untuk mendukung proses pembelajaran akuntansi
                    secara efektif.

                </div>

            </div>
            """,
            unsafe_allow_html=True
        )

    with right:

        st.image(
            "assets/logo.png",
            width=140
        )
