class Functions:
    @staticmethod
    def printOptions():
        """
        Function that prints possible options
        of questionary: A, B or C
        """
        print("(A) Never or seldom")
        print("(B) Sometimes")
        print("(C) Always or almost always\n")

    @staticmethod
    def questionaryTotal(choice, points):
        """
        Function that take user choice and current points
        and return the sum of points depends on choice
        """
        if choice.upper() == "A":
            points = points + 1
        elif choice.upper() == "B":
            points = points + 0.5
        return points

    @staticmethod
    def questionaryResult(points):
        """
        Function that prints the result
        depending of sum of points
        """
        if points >= 0 and points <= 2:
            print("Low: You are the new Terminator model Roomba TX6000")
        elif points > 2 and points <= 5:
            print("Medium: So, you are 'normal'")
        elif points > 5 and points <= 8:
            print("High: Don't do today what you can do tomorrow!")
        else:
            print("Extreme: You even procrastinate this questionary for hours!")
