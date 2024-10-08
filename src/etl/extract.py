import gspread
from google.oauth2.service_account import Credentials
import json
from tqdm import tqdm
import time
from src.helpers import common

# Load credentials from the JSON key file you downloaded
SCOPES = ["https://www.googleapis.com/auth/spreadsheets",
          "https://www.googleapis.com/auth/drive"]
CREDS = Credentials.from_service_account_file(
    'src/configs/google_sheet_api.json', scopes=SCOPES)

# GGSHEET_TITLE = 'HeyJapan_Dữ liệu tiếng Việt_N3'
GGSHEET_TITLE = 'HeyJapan_Dữ liệu tiếng Việt_Trung cấp'
DATA = 'src/data'


def extract_data():
    # Authorize with the credentials
    client = gspread.authorize(CREDS)

    # Open a specific Google Sheet by title
    sheet = client.open(GGSHEET_TITLE)
    worksheets = sheet.worksheets()
    sheet_names = [sheet.title for
                   sheet in worksheets if common.is_number(sheet.title[0]) and (
                       sheet.title == "225_Nguyên nhân (6)" or 
                       sheet.title == "226_Kinh tế - Chính trị - Xã hội" or 
                       sheet.title == "227_Mặc dù ~" or 
                       sheet.title == "228_Cùng với ~" or 
                       sheet.title == "229_May mắn"
                )]
    # sheet_names = [sheet.title for
    #                sheet in worksheets if common.is_number(sheet.title[0]) and (sheet.title != "131_Nhờ vả" and sheet.title != "139_Miêu tả (2)" and sheet.title != "140_Xin phép (2)" and sheet.title != "143_Mong muốn (2)" and sheet.title != "145_Truyền đạt thông tin (2)" and sheet.title != "146_Ngôn ngữ nói (1)" and sheet.title != "148_Kết nối (2)")]
    chunk_size = 30
    seperate_sheets = [sheet_names[i:i+chunk_size]
                       for i in range(0, len(sheet_names), chunk_size)]
    for seperate_sheet in seperate_sheets:
        for sheet_name in tqdm(seperate_sheet):
            worksheet_data = sheet.worksheet(sheet_name)
            all_records_worksheet_data = worksheet_data.get_all_records()
            for index, tmp in enumerate(all_records_worksheet_data):
                if (index == 0):
                    continue
                tmp["Unit"] = tmp["Unit"] if bool(
                    tmp["Unit"]) else all_records_worksheet_data[index-1]["Unit"]

            save_data_to_json(all_records_worksheet_data,
                              f'{DATA}/{sheet_name}.json')
    return GGSHEET_TITLE, sheet_names


def save_data_to_json(data, path, type=''):
    with open(path, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)
