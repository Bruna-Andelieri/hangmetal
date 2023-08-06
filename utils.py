import os

ROWSIZE = 80


def clear_terminal():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

