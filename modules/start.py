"""
import library time, functions and utils
"""

from .utils import Utils
from .functions import Functions


class Start:
    """
    main(): initiates the questionary
    """

    # default constructor

    def __init__(self):
        self.sum_points = 0
        self.user_answers = []
        self.list_questions = Functions.shuffle_questions()
        Utils.cls()

    def main(self):
        """
        Function that open gspread of questionary
        random choose 10 questions of file text
        gather all input question choice
        and calculate the total and result
        """
        Functions.print_intro()
        Functions.press_enter_continue()
        Utils.cls()
        self.sum_points = Functions.run_questionary(
            self.list_questions, self.user_answers, self.sum_points
        )
        Functions.print_user_result(self.sum_points)
        Functions.print_total_result()
