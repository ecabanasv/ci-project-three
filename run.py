# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import random
from turtle import clear
import gspread
import os
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

# Function that clears the console windows or linux (reference: https://stackoverflow.com/questions/517970/how-to-clear-the-interpreter-console)
def cls():
    os.system('cls' if os.name=='nt' else 'clear')


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

def questionaryTotal(choice, puntos):
    
    if choice == "A":
        puntos = puntos + 1
    elif choice == "B":
        puntos = puntos + 0.5
    return puntos


def inputRandomizeQuestions():
    f = open("q1.txt", "r")
    list = []
    answers = []
    puntos = 0
    for i in f:
        list.append(i)
    random.shuffle(list)
    for i in range(10):
        print(list[i])
        printOptions()
        a = input("Enter your choice: ")
        puntos = questionaryTotal(a, puntos)
        print("\n")
        answers.append(a)
        cls()
    print(puntos)


inputRandomizeQuestions()










