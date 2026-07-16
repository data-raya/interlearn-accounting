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