import random

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
            "Are you a procrastinator? The following questionnaire",
            " will let you know if you are a born procrastinator.\n",
        )
        print(
            "Please, take your time to answer the questions.",
            "There will be three options (A, B and C)\n"
        )
        print(
            "At the end of questionary we will show the results,",
            "and the total results (if available).\n"
        )

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
    def questionary_result(points):
        """
        Function that prints the result
        depending of sum of points
        """
        print("YOUR RESULTS:\n")
        if points >= 0 and points <= 2:
            print("  (Low) You scored " + str(points) + " points.",
            "You are the new Terminator model Roomba TX6000")
        elif points > 2 and points <= 5:
            print("  (Medium) You scored " + str(points) + " points.",
            "We suppose that you are 'normal'")
        elif points > 5 and points <= 8:
            print("  (High) You scored " + str(points) + " points.",
            "Don't do today what you can do tomorrow!")
        else:
            print("  (Extreme) You scored " + str(points) + " points.",
            "You even procrastinate this questionary for hours!")

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
