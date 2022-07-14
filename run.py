# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('ci-p3-sheet')

weight = SHEET.worksheet('weight')
img = SHEET.worksheet('img')
diff_img = SHEET.worksheet('diff_img')


def exist_username():
    """
    Get username if exist in the sheet
    If not request to create a new one
    """
    val = weight.acell('A2').value
    if val is not None:
        return "true"


def get_create_username():
    """
    Get username if exist in the sheet
    If not request to create a new one
    """
    if exist_username() != "true":
        print("No users registered. Please register your username:")
    else:
        print("Register (R) / Access user (A):")


get_create_username()