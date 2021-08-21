"""This module holds all validation functions needed for use with run.py. Each
function is responsible for validating a different type of data."""


def validate_choice(prompt, option_1, option_2):
    """
    Validate user input for a question with 2 possible answers, alerting
    them if input is somehow invalid.

    Args:
    prompt: Question to ask the user.
    option_1: First option that the user can choose.
    option_2: Second option user that the use can choose.

    Returns:
    User input, when valid.
    """

    while True:
        user_input = input(prompt).lower()
        if user_input in (option_1, option_2):
            return user_input
        print(
            "\nInvalid input! Please try again.\n")


def validate_count(user_input, available_posts):
    """
    Get positive number from user, checking input is below maximum available
    posts and returning number if so.

    Args:
    user_input: Input given by the user. Should be a number.
    available_posts: Amount of posts available to be displayed.

    Returns:
    True or False, depending on whether input is valid, or raises exception if 
    input is not a number. 
    """

    try:
        count = int(user_input)
        if 0 <= count <= available_posts:
            return True
        return False
    except ValueError:
        raise
