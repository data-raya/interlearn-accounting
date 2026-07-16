from datetime import datetime
import streamlit as st
import gspread
import os
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

    # cek apakah sudah pernah selesai
    for i, row in enumerate(data, start=2):

        if (
            row["ID User"] == id_user and
            row["ID Materi"] == id_materi
        ):

            sheet.update(
                f"D{i}:E{i}",
                [[
                    "TRUE",
                    datetime.now().strftime("%Y-%m-%d")
                ]]
            )

            return

    # kalau belum ada -> tambah baris baru

    id_progress = f"PR{len(data)+1:03d}"

    sheet.append_row([

        id_progress,
        id_user,
        id_materi,
        "TRUE",
        datetime.now().strftime("%Y-%m-%d")

    ])