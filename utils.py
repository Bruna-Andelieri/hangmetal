"""
This file contains the clear function, allowing other files
to access it without needing to rewrite it.
"""

import os


def clear_terminal():
    """
    clear the terminal
    """
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
