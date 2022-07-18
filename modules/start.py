import random
import time

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
    """
    main(): initiates the questionary
    """

    @staticmethod
    def main():
        """
        Function that open gspread of questionary
        random choose 10 questions of file text
        gather all input question choice
        and calculate the total and result
        """
        user_answers = []
        list_questions = []
        sum_points = 0
        Utils.cls()
        Functions.printIntro()
        time.sleep(5)
        Utils.cls()
        list_questions = Functions.shuffle_questions()

        for i in range(10):
            print(Fore.YELLOW + list_questions[i])
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
        print(sum_points)
        user_answers.append(sum_points)
        Functions.questionaryResult(sum_points)
        Q1.append_row(user_answers)
        values_list = Q1.col_values(11, value_render_option="UNFORMATTED_VALUE")
        values_list.remove("result")
        print("There were", len(values_list), "participants in total.")
        print(
            "Average of all participants is",
            round(sum(values_list) / len(values_list), 2),
        )
