"""
Import library os
"""
import os


class Utils:
    """
    Library of useful functions
    """

    @staticmethod


    def cls():
        """
        Function that clears the console windows or linux
        """
        os.system("cls" if os.name == "nt" else "clear")
        