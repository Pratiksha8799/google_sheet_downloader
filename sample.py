import os
import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials

class Sheet_Downloader:
    def __init__(self, creds_file, sheet_url):
        self.creds_file = creds_file
        self.sheet_url = sheet_url
        self.client = self.authenticate_google()

    # Function to authenticate using Google credentials
    def authenticate_google(self):
        scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
        creds = ServiceAccountCredentials.from_json_keyfile_name(self.creds_file, scope)
        client = gspread.authorize(creds)
        return client

    # Function to download Google Sheet data
    def download_google_sheet(self, file_format, output_file='output'):
        # Authenticate and access the sheet
        sheet = self.client.open_by_url(self.sheet_url).sheet1  # Access the first sheet

        # Get all data in the sheet as a list of dictionaries
        data = sheet.get_all_records()

        # Convert data to a Pandas DataFrame
        df = pd.DataFrame(data)

        # Save DataFrame as CSV or Excel based on file format
        if file_format == 'csv':
            output_file += '.csv'
            df.to_csv(output_file, index=False)
            print(f"Google Sheet data saved as CSV: {output_file}")
        elif file_format == 'excel':
            output_file += '.xlsx'
            df.to_excel(output_file, index=False)
            print(f"Google Sheet data saved as Excel: {output_file}")
        else:
            print("Unsupported file format. Use 'csv' or 'excel'.")

if __name__ == "__main__":
    creds_file = os.getenv('CREDS_FILE')
    sheet_url = os.getenv('SHEET_URL')

    if not creds_file or not sheet_url:
       raise ValueError("CREDS_FILE or SHEET_URL environment variables not set")

    s = Sheet_Downloader(creds_file, sheet_url)
    # Choose the output format: 'csv' or 'excel'
    file_format = 'csv'  # or 'excel'

    # Output filename without extension
    output_file = 'google_sheet_data'

    # Correct call to download Google Sheet data
    s.download_google_sheet(file_format, output_file)
