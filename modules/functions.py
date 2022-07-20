import random
import gspread
from google.oauth2.service_account import Credentials
from colorama import Fore

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


class Functions:
    """
    Contains main functions used in start.py
    """

    @staticmethod
    def print_intro():
        """
        Function that prints introduction text
        """
        print(
            Fore.GREEN + "Are you a procrastinator? The following questionnaire",
            " will let you know if you are a born procrastinator.\n",
        )
        print(
            Fore.GREEN + "Please, take your time to answer the questions.",
            "Choose options A, B or C.\n",
        )
        print(
            Fore.GREEN + "At the end of questionary we will show the results,",
            "and the total results.\n",
        )

    @staticmethod
    def gspread_add_row_questionary(row):
        """
        Function that add row with answers and points in Google Sheet Q1
        """
        Q1.append_row(row)

    @staticmethod
    def run_questionary(questions, row, points):
        """
        Function that run the questionary (10 questions)
        After calculate questionary points and call function to add to gspread Q1
        """
        for i in range(10):
            print(Fore.YELLOW + questions[i])
            Functions.print_options()
            while True:
                user_input = input(Fore.WHITE + "Enter your choice: ")
                if user_input.upper() in ["A", "B", "C"]:
                    break
                print(Fore.RED + "Please enter characters A, B or C only")
            points = Functions.questionary_total(user_input, points)
            print("\n")
            row.append(user_input.upper())
        row.append(points)
        Functions.gspread_add_row_questionary(row)

    @staticmethod
    def print_options():
        """
        Function that prints possible options
        of questionary: A, B or C
        """
        print("(A) Never or seldom")
        print("(B) Sometimes")
        print("(C) Always or almost always\n")

    @staticmethod
    def questionary_total(choice, points):
        """
        Function that take user choice and current points
        and return the sum of points depends on choice
        """
        if choice.upper() == "B":
            points = points + 0.5
        elif choice.upper() == "C":
            points = points + 1
        return points

    @staticmethod
    def print_user_result(points):
        """
        Function that prints the result
        depending of sum of points
        """
        print(Fore.MAGENTA + "YOUR RESULTS:\n")
        if points >= 0 and points <= 2:
            print(
                Fore.WHITE + "  (Low) You scored " + str(points) + " points.",
                "You are the new Terminator model Roomba TX6000",
            )
        elif points > 2 and points <= 5:
            print(
                Fore.WHITE + "  (Medium) You scored " + str(points) + " points.",
                "We suppose that you are 'normal'",
            )
        elif points > 5 and points <= 8:
            print(
                Fore.WHITE + "  (High) You scored " + str(points) + " points.",
                "Don't do today what you can do tomorrow!",
            )
        else:
            print(
                Fore.WHITE + "  (Extreme) You scored " + str(points) + " points.",
                "You even procrastinate this questionary for hours!",
            )

    @staticmethod
    def print_total_result():
        """
        Functions that print results on screen after finish Q1
        """
        values_list = Q1.col_values(11, value_render_option="UNFORMATTED_VALUE")
        values_list.remove("result")
        if len(values_list) > 1:
            print(Fore.MAGENTA + "\nTOTAL:\n")
            print(
                Fore.WHITE
                + "  There are "
                + str(len(values_list))
                + " participants in total",
                "with an average of "
                + str(round(sum(values_list) / len(values_list), 2))
                + " points.\n",
            )

    @staticmethod
    def shuffle_questions():
        """
        Open file q1.txt
        Add questions to list_questions
        return Shuffle questions
        """
        f = open("q1.txt")
        list_questions = []
        for i in f:
            list_questions.append(i)
        random.shuffle(list_questions)
        return list_questions
