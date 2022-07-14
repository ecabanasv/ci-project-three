# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import random
import os
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

def cls():
    """
    Function that clears the console windows or linux 
    Reference: https://stackoverflow.com/questions/517970/how-to-clear-the-interpreter-console
    """
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
    """
    Function that prints possible options
    of questionary: A, B or C
    """
    print("(A) Never or seldom")
    print("(B) Sometimes")
    print("(C) Always or almost always\n")

def questionaryTotal(choice, puntos):
    """
    Function that take user choice and current points
    and return the sum of points depends on choice
    """
    if choice.upper() == "A":
        puntos = puntos + 1
    elif choice.upper() == "B":
        puntos = puntos + 0.5
    return puntos

def questionaryResult(puntos):
    """
    Function that prints the result
    depending of sum of points
    """
    if puntos >= 0 and puntos <= 2:
        print("Low")
    elif puntos > 2 and puntos <= 5:
        print("Medium")
    elif puntos > 5 and puntos <= 8:
        print("High")
    else:
        print("Extreme")

def inputRandomizeQuestions():
    """
    Function that open gspread of questionary
    random choose 10 questions of file text
    gather all input question choice
    and calculate the total and result
    """
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
        while True:
            a = input("Enter your choice: ")
            if a.upper() in ["A","B","C"]:
                break
            print("Please enter characters A, B or C only")
        puntos = questionaryTotal(a, puntos)
        print("\n")
        answers.append(a)
        #cls()
    questionaryResult(puntos)
    print(puntos)
    print(answers)


inputRandomizeQuestions()










