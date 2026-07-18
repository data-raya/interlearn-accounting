import streamlit as st

from database.database import (
    get_quiz_by_materi,
    simpan_hasil_quiz
)


def quiz_page():

    # Pastikan user memilih materi
    if "id_materi" not in st.session_state:

        st.warning("Materi tidak ditemukan.")

        return

    # Ambil semua soal sesuai materi
    if (
        "quiz_data" not in st.session_state
        or st.session_state.get("quiz_materi") != st.session_state.id_materi
    ):

        st.session_state.quiz_data = get_quiz_by_materi(
            st.session_state.id_materi
        )

        st.session_state.quiz_materi = st.session_state.id_materi

    quiz = st.session_state.quiz_data

    # Kalau belum ada soal
    if len(quiz) == 0:

        st.warning("Quiz belum tersedia.")

        return

    # Session soal
    if "nomor_soal" not in st.session_state:

        st.session_state.nomor_soal = 0

    if "jawaban_quiz" not in st.session_state:

        st.session_state.jawaban_quiz = {}

    nomor = st.session_state.nomor_soal

    soal = quiz[nomor]

    st.title("📝 Quiz")

    st.caption(
        f"Soal {nomor+1} dari {len(quiz)}"
    )

    st.divider()

    st.subheader(soal["Soal"])

    opsi = [

        soal["Pilihan A"],
        soal["Pilihan B"],
        soal["Pilihan C"],
        soal["Pilihan D"]

    ]

    jawaban_sebelumnya = st.session_state.jawaban_quiz.get(nomor)

    if jawaban_sebelumnya in opsi:

        index = opsi.index(jawaban_sebelumnya)

    else:

        index = None

    pilihan = st.radio(

        "Pilih Jawaban",

        opsi,

        index=index,

        key=f"radio_{nomor}"

    )

    # ==========================
    # Simpan Jawaban User
    # ==========================

    if pilihan:

        st.session_state.jawaban_quiz[nomor] = pilihan

    st.divider()

    col1, col2 = st.columns(2)

    with col1:

        if st.button(
            "⬅ Previous",
            disabled=nomor == 0
        ):

            st.session_state.nomor_soal -= 1

            st.rerun()

    with col2:

        if nomor < len(quiz)-1:

            if st.button(
                "Next ➡",
                use_container_width=True
            ):

                st.session_state.nomor_soal += 1

                st.rerun()

        else:

            st.success("🎉 Semua soal telah ditampilkan.")

            if st.button(
                "✅ Submit Quiz",
                use_container_width=True,
                type="primary"
            ):

                benar = 0

                for i, item in enumerate(quiz):

                    jawaban_user = st.session_state.jawaban_quiz.get(i)

                    jawaban_benar = item["Jawaban"]

                    jawaban_benar = item[f"Pilihan {item['Jawaban']}"]

                    if jawaban_user == jawaban_benar:

                        benar += 1

                salah = len(quiz) - benar

                nilai = round((benar / len(quiz)) * 100)

                st.session_state.nilai = nilai

                st.session_state.benar = benar

                st.session_state.salah = salah

                simpan_hasil_quiz(

                    st.session_state.user_id,

                    st.session_state.id_materi,

                    nilai,

                    benar,

                    salah

                )

                st.session_state.pop("quiz_data", None)
                st.session_state.pop("quiz_materi", None)

                st.session_state.page = "hasil"

                st.rerun()