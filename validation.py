"""This module holds all validation functions needed for use with run.py. Each
function is responsible for validating a different type of data."""


def validate_choice(prompt, option_1, option_2):
    """Validate user input for a question with 2 possible answers, alerting
    them if input is somehow invalid."""

    while True:
        user_input = input(prompt).lower()
        if user_input in (option_1, option_2):
            return user_input
        print(
            "\nInvalid input! Please make sure all input is correct and in lowercase.\n")


def validate_count(input, available_posts):
    """Get positive number from user, checking input is below maximum available
    posts and returning number if so."""

    try:
        count = int(input)
        if 1 <= count <= available_posts:
            return True
        return False
    except ValueError:
        raise


def validate_http(trending, newest):
    """Check HTTP status code of both required links for app to function"""

    return trending.status_code == 200 and newest.status_code == 200
