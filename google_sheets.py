import os
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
from dotenv import load_dotenv

load_dotenv()

def upload_to_google_sheets(df):
    sheet_id = os.getenv("SHEET_ID")
    creds = Credentials.from_service_account_file("google-creds.json", scopes=["https://www.googleapis.com/auth/spreadsheets"])

    service = build("sheets", "v4", credentials=creds)
    sheet = service.spreadsheets()

    values = [df.columns.tolist()] + df.astype(str).values.tolist()

    sheet.values().append(
        spreadsheetId=sheet_id,
        range="Sheet1!A1",
        valueInputOption="RAW",
        insertDataOption="INSERT_ROWS",
        body={"values": values}
    ).execute()
