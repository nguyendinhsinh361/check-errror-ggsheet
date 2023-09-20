import gspread
from google.oauth2.service_account import Credentials
import json
import requests
from bs4 import BeautifulSoup
import re

# Load credentials from the JSON key file you downloaded
SCOPES = ["https://www.googleapis.com/auth/spreadsheets",
          "https://www.googleapis.com/auth/drive"]
CREDS = Credentials.from_service_account_file(
    'src/configs/google_sheet_api.json', scopes=SCOPES)

GGSHEET_TITLE = '[HeyJapan] Dữ liệu bài học Đức'

GGSHEET_FRANCE = 'HeyFrance'

DATA_FRANCE = 'static/france.json'


def extract_data():
    # Authorize with the credentials
    client = gspread.authorize(CREDS)

    # Open a specific Google Sheet by title
    sheet = client.open(GGSHEET_TITLE)

    # Select a specific worksheet within the Google Sheet
    worksheet_w1 = sheet.worksheet(GGSHEET_FRANCE)

    all_records_w1 = worksheet_w1.get_all_records()

    save_data_to_json(all_records_w1, DATA_FRANCE)


def save_data_to_json(data, path, type=''):
    with open(path, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)
