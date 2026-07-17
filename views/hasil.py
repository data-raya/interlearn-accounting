import streamlit as st

def hasil_page():

    st.title("🏆 Hasil Quiz")

    st.metric(

        "Nilai",

        st.session_state.nilai

    )

    col1, col2 = st.columns(2)

    with col1:

        st.metric(

            "Benar",

            st.session_state.benar

        )

    with col2:

        st.metric(

            "Salah",

            st.session_state.salah

        )

    st.divider()

    if st.button(

        "🏠 Kembali ke Dashboard",

        use_container_width=True

    ):

        st.session_state.nomor_soal = 0

        st.session_state.jawaban_quiz = {}

        st.session_state.page = "home"

        st.rerun()