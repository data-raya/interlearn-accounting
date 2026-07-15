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

    # Jika dijalankan di laptop
    if os.path.exists("config/credentials.json"):

        creds = Credentials.from_service_account_file(
            "config/credentials.json",
            scopes=SCOPES
        )

    # Jika dijalankan di Streamlit Cloud
    else:

        creds = Credentials.from_service_account_info(
            dict(st.secrets),
            scopes=SCOPES
        )


    client = gspread.authorize(creds)

    return client.open_by_key(SPREADSHEET_ID)



def get_materi():

    sheet = connect_sheet().worksheet("Materi")

    return sheet.get_all_records()