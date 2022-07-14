# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import random
import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive",
]

CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("ci-pp3-sheet")

Q1 = SHEET.worksheet("Q1")


# def check_user_exist():
#     """
#     Get username if exist in the sheet
#     If not request to create a new one
#     """
#     val = Q1.acell("A2").value
#     if val is not None:
#         return "true"

# def reg_new_user():

# def access_reg_user():


# def reg_or_access_user():
#     """
#     Get username if exist in the sheet
#     If not request to create a new one
#     """
#     if check_user_exist() != "true":
#         reg_new_user()
#     else:
#         access_reg_user()


# reg_or_access_user()

def printOptions():
    print("(A) Never or seldom")
    print("(B) Sometimes")
    print("(C) Always or almost always\n")


def inputRandomizeQuestions():
    f = open("q1.txt", "r")
    list = []
    answers = []
    for i in f:
        list.append(i)
    random.shuffle(list)
    for i in range(10):
        print(list[i])
        printOptions()
        a = input("Enter your choice: ")
        print("\n")
        answers.append(a)

    for i in range(10):
        print(answers[i])


inputRandomizeQuestions()










