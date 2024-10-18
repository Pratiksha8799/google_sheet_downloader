
# Google Sheet Downloader

This Python script allows users to download data from a specified Google Sheet and save it in either CSV or Excel format. It utilizes the gspread library for interacting with Google Sheets and pandas for data manipulation and saving.

## Dependencies

To run this script, you need to have the following libraries installed:

* gspread

* oauth2client

* pandas

You can install these libraries using pip:
```bash
pip install gspread oauth2client pandas
```
#### Note: Ensure that the service account associated with the credentials JSON file has been granted access to the Google Sheet you wish to download. Set environment variables for CREDS_FILE and SHEET_URL in your system


### How to set Environment Variables in Your System

[Article](https://medium.com/@pratiksha.garkar/how-to-set-environment-variables-in-your-system-86361e3163e1)
## Methods

1. authenticate_google(): Authenticates the Google Service Account using the provided credentials and returns a client for accessing Google Sheets.

Returns: gspread.Client instance for interacting with Google Sheets.

2. download_google_sheet(file_format, output_file='output'): Downloads data from the specified Google Sheet and saves it in the desired format (CSV or Excel).


* Parameters:

    a. file_format: Desired file format for saving the data. Acceptable values are 'csv' or 'excel'.



    b. output_file: Name of the output file without the extension. Default is 'output'.


## Process:
* Accesses the first sheet of the Google Sheet.

* Retrieves all records as a list of dictionaries.

* Converts the list to a Pandas DataFrame.

* Saves the DataFrame as either a CSV or Excel file based on the specified format.
## Potential Users

* Data Analysts: Analysts who need to regularly extract data from Google Sheets for analysis or reporting.

* Data Scientists: Data scientists who require automated data extraction as part of their data preprocessing pipeline.

## Use Cases
* Automated Reporting: Users can automate the download of data for reporting purposes, saving time and effort.

* Data Migration: Users might use the script to migrate data from Google Sheets to local files for further processing.

## Conclusion
A straightforward yet effective method for obtaining data from Google Sheets and storing it in CSV or Excel format is offered by the Google Sheet Downloader project. The script facilitates smooth interaction with Google Sheets and effortless data manipulation by utilizing the Google Sheets API and the capabilities of gspread and pandas.





## Support

For support, email pratikshagarkar871999@gmail.com

[![Medium](https://img.shields.io/badge/Medium-000?style=for-the-badge&logo=medium&logoColor=white)](https://medium.com/@pratiksha.garkar)


[![Kaggle](https://img.shields.io/badge/Kaggle-000?style=for-the-badge&logo=kaggle&logoColor=white)](https://www.kaggle.com/pratikshagarkar)

[![LinkedIn](https://img.shields.io/badge/LinkedIn-000?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/pratiksha-garkar-110a9a171/)



