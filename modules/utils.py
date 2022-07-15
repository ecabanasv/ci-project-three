import os


class Utils:
    """
    Useful functions
    """

    @staticmethod
    def cls():
        """
        Function that clears the console windows or linux
        Reference: https://stackoverflow.com/questions/517970/how-to-clear-the-interpreter-console
        """
        os.system("cls" if os.name == "nt" else "clear")
