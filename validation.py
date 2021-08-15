def validate_choice(prompt, option_1, option_2):
    """Validate user input for a question with 2 possible answers, alerting 
    them if input is somehow invalid."""

    while True:
        user_input = input(prompt).lower()
        if user_input in (option_1, option_2):
            return user_input
        print(
            "\nInvalid input! Please make sure all input is correct and in lowercase.\n")


def validate_count(available_posts):
    """Get positive number from user, checking input is below maximum available 
    posts and returning number if so."""

    while True:
        try:
            count = int(
                input(f"\nHow many posts do you want to see? ({available_posts} available)\n"))

            if 1 <= count <= available_posts:
                return count

            if available_posts == 1:
                print("\nOnly 1 post left to show.")
                continue

            print(f"\nPlease enter a number between 1 and {available_posts}.")
        except ValueError:
            print("\nPlease enter a number.")


def validate_http(trending, newest):
    """Check HTTP status code of both required links for app to function"""

    return trending.status_code == 200 and newest.status_code == 200
