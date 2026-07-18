from datetime import datetime
import time 
import streamlit as st
import gspread
import os
import traceback
from google.oauth2.service_account import Credentials


SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]


SPREADSHEET_ID = "1_zhagRE9eqIWWetdRsXz8zmrMKe1ryBnad77kEzicAg"

@st.cache_resource
def connect_sheet():

    for i in range(3):

        try:

            if os.path.exists("config/credentials.json"):

                creds = Credentials.from_service_account_file(
                    "config/credentials.json",
                    scopes=SCOPES
                )

            else:

                creds = Credentials.from_service_account_info(
                    st.secrets["gcp_service_account"],
                    scopes=SCOPES
                )

            client = gspread.authorize(creds)

            return client.open_by_key(SPREADSHEET_ID)

        except Exception:

            if i == 2:
                raise

            time.sleep(2)

@st.cache_data(ttl=300)
def get_materi():

    sheet = connect_sheet().worksheet("Materi")

    return sheet.get_all_records()

@st.cache_data(ttl=300)
def get_users():

    sheet = connect_sheet().worksheet("Users")

    return sheet.get_all_records()


@st.cache_data(ttl=300)
def get_user_progress_data():

    sheet = connect_sheet().worksheet("UserProgress")

    return sheet.get_all_records()


@st.cache_data(ttl=300)
def get_user_quiz_data():

    sheet = connect_sheet().worksheet("UserQuiz")

    return sheet.get_all_records()

def get_materi_by_kategori(kategori):

    data = get_materi()

    hasil = []

    for row in data:

        if row["Kategori"] == kategori:

            hasil.append(row)

    return hasil

def get_materi_by_id(id_materi):

    data = get_materi()

    for item in data:
        if item["ID Materi"] == id_materi:
            return item

    return None

def convert_drive_preview(url):

    file_id = url.split("/d/")[1].split("/")[0]

    return f"https://drive.google.com/file/d/{file_id}/preview"

def selesai_membaca(id_user, id_materi):

    sheet = connect_sheet().worksheet("UserProgress")

    data = sheet.get_all_records()

    # Cek apakah user sudah menyelesaikan materi
    for row in data:

        if (
            row["ID User"] == id_user and
            row["ID Materi"] == id_materi
        ):
            return

    # Generate ID Progress
    id_progress = f"PR{len(data)+1:03d}"

    # Simpan ke Google Sheet
    sheet.append_row([
        id_progress,
        id_user,
        id_materi,
        "TRUE",
        datetime.now().strftime("%Y-%m-%d")
    ])

def login_user(email, password):

    data = get_users()

    for user in data:

        if (
            user["Email"] == email and
            user["Password"] == password
        ):

            return user

    return None

def register_user(nama, email, password):

    sheet = connect_sheet().worksheet("Users")

    data = get_users()

    # Cek apakah email sudah dipakai
    for user in data:

        if user["Email"] == email:

            return False

    # Buat ID User baru
    id_user = f"U{len(data)+1:03d}"

    # Tambahkan ke Google Sheet
    sheet.append_row([
        id_user,
        nama,
        email,
        password
    ])

    get_users.clear()

    return True

def get_user_progress(id_user):

    data = get_user_progress_data()

    hasil = []

    for row in data:

        if row["ID User"] == id_user:

            hasil.append(row)

    return hasil

def sudah_selesai_materi(id_user, id_materi):

    progress = get_user_progress(id_user)

    for row in progress:

        if row["ID Materi"] == id_materi:
            return True

    return False

def get_progress_kategori(id_user, kategori):

    materi = get_materi_by_kategori(kategori)

    progress = get_user_progress(id_user)

    materi_selesai = []

    for row in progress:
        materi_selesai.append(row["ID Materi"])

    selesai = sum(
        1
        for item in materi
        if item["ID Materi"] in materi_selesai
    )

    return selesai

def get_quiz_by_materi(id_materi):

    sheet = connect_sheet().worksheet("Quiz")

    data = sheet.get_all_records()

    hasil = []

    for row in data:

        if row["ID Materi"] == id_materi:

            hasil.append(row)

    hasil.sort(key=lambda x: int(x["Nomor Soal"]))

    return hasil

def simpan_hasil_quiz(
    id_user,
    id_materi,
    nilai,
    benar,
    salah
):

    sheet = connect_sheet().worksheet("UserQuiz")

    data = sheet.get_all_records()

    # Cek apakah sudah pernah quiz
    for row in data:

        if (
            row["ID User"] == id_user and
            row["ID Materi"] == id_materi
        ):

            return

    id_hasil = f"UQ{len(data)+1:03d}"

    sheet.append_row([

        id_hasil,

        id_user,

        id_materi,

        nilai,

        benar,

        salah,

        "Lulus" if nilai >= 70 else "Tidak Lulus",

        datetime.now().strftime("%Y-%m-%d")

    ])

    get_user_progress_data.clear()

def get_user_quiz(id_user):

    data = get_user_quiz_data()

    hasil = []

    for row in data:

        if row["ID User"] == id_user:

            hasil.append(row)

    return hasil

def get_rata_rata_quiz(id_user):

    quiz = get_user_quiz(id_user)

    if len(quiz) == 0:
        return 0

    total = sum(int(item["Nilai"]) for item in quiz)

    return round(total / len(quiz)) 

def cek_sudah_quiz(id_user, id_materi):

    data = get_user_quiz(id_user)

    for row in data:

        if row["ID Materi"] == id_materi:

            return True

    return False

def get_hasil_quiz(id_user, id_materi):

    data = get_user_quiz(id_user)

    for row in data:

        if row["ID Materi"] == id_materi:

            return row

    return None

def get_user_by_id(id_user):

    data = get_users()

    for row in data:

        if row["ID User"] == id_user:

            return row

    return None