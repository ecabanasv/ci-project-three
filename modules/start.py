import random
from .utils import Utils
from .functions import Functions
from colorama import Fore
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

class Start:

    @staticmethod
    def main():
        """
        Function that open gspread of questionary
        random choose 10 questions of file text
        gather all input question choice
        and calculate the total and result
        """
        f = open("q1.txt", "r")
        list_questions = []
        user_answers = []
        sum_points = 0
        for i in f:
            list_questions.append(i)
        random.shuffle(list_questions)
        for i in range(10):
            print(Fore.CYAN + list_questions[i])
            Functions.printOptions()
            while True:
                user_input = input(Fore.WHITE + "Enter your choice: ")
                if user_input.upper() in ["A", "B", "C"]:
                    break
                print(Fore.RED + "Please enter characters A, B or C only")
            sum_points = Functions.questionaryTotal(user_input, sum_points)
            print("\n")
            user_answers.append(user_input.upper())
            Utils.cls()
        user_answers.append(sum_points)
        Functions.questionaryResult(sum_points)
        print(sum_points)
        print(user_answers)
        Q1.append_row(user_answers)
