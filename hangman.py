"""
File responsible for maintaining the displayed hangman throughout all attempts.

"""


def display_hangman(attempts):
    """
    Display the stages of the hangman
    """
    stages = [  # final state: head, torso, both arms, and both legs
        """
--------
|      |
|      O
|     \\|/
|      |
|     / \\
-----------
""",
        # head, torso, both arms, and one leg
        """
--------
|      |
|      O
|     \\|/
|      |
|     /
-----------
""",
        # head, torso, and both arms
        """
--------
|      |
|      O
|     \\|/
|      |
|
-----------
""",
        # head, torso, and one arm
        """
--------
|      |
|      O
|     \\|
|      |
|
-----------
""",
        # head and torso
        """
--------
|      |
|      O
|      |
|      |
|
-----------
""",
        # head
        """
--------
|      |
|      O
|
|
|
-----------
""",
        # initial empty state
        """
--------
|      |
|
|
|
|
-----------
""",
    ]
    return stages[attempts]
