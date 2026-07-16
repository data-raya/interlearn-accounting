from datetime import datetime
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


def connect_sheet():

    # Local
    if os.path.exists("config/credentials.json"):

        creds = Credentials.from_service_account_file(
            "config/credentials.json",
            scopes=SCOPES
        )

    # Streamlit Cloud
    else:

        creds = Credentials.from_service_account_info(
            st.secrets["gcp_service_account"],
            scopes=SCOPES
        )

    client = gspread.authorize(creds)

    return client.open_by_key(SPREADSHEET_ID)

@st.cache_data(ttl=300)
def get_materi():

    sheet = connect_sheet().worksheet("Materi")

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

    sheet = connect_sheet().worksheet("Users")

    data = sheet.get_all_records()

    for user in data:

        if (
            user["Email"] == email and
            user["Password"] == password
        ):

            return user

    return None

def register_user(nama, email, password):

    sheet = connect_sheet().worksheet("Users")

    data = sheet.get_all_records()

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

    return True

def get_user_progress(id_user):

    sheet = connect_sheet().worksheet("UserProgress")

    data = sheet.get_all_records()

    hasil = []

    for row in data:

        if row["ID User"] == id_user:

            hasil.append(row)

    return hasil

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