import sys
import requests
from bs4 import BeautifulSoup
from validation import validate_choice, validate_count

TRENDING_URL = "https://news.ycombinator.com/news"
NEWEST_URL = "https://news.ycombinator.com/newest"


class Posts:
    """Responsible for preparing and organising post data, given a Hacker News
    URL."""

    def __init__(self, url):
        self.url = url

    def get_info(self):
        """
        Fetch post data from HTML, adding all data into list of dictionaries.

        Returns:
        List containing a dictionary for each post (30 posts total).
        """

        response = requests.get(self.url)
        html = BeautifulSoup(response.text, "html.parser")

        html_titles = html.find_all(class_="titlelink")
        html_ages = html.find_all(class_="age")

        li = []
        for i in range(30):  # 30 is a full page of posts
            di = {}
            di["title"] = html_titles[i].text
            di["link"] = html_titles[i]["href"]
            di["age"] = html_ages[i].text
            li.append(di)
        return li


class Printer():
    """Responsible for the handling and printing of post data in the
    application."""

    def __init__(self, posts):
        self.posts = posts

    def request_more(self, available_posts):
        """
        Ask user if they want to view more posts and, if so, how many.

        Args:
        available_posts: Amount of posts available to be displayed.

        Returns:
        Amount of posts user wishes to see.
        """

        user_input = validate_choice(
            "Do you want to see more posts? (yes / no):\n", "yes", "no")
        if user_input == "no":
            return False
        return get_post_count(available_posts)

    def print_info(self, count):
        """
        Print initially requested post information to the terminal and ask
        the user if they want to view more posts using request_more function.

        Args:
        count: Amount of posts the user wishes to see.

        Returns:
        User's requested posts.
        """

        shown_posts = 0
        to_show = count

        while True:
            for i in self.posts[shown_posts: shown_posts + to_show]:
                print(f"\n{self.posts.index(i) + 1}) Title: {i['title']}")
                print(f"Link: {i['link']}")
                print(f"Posted: {i['age']}\n")

            shown_posts += to_show
            if shown_posts == 30:
                print("No more posts to show.")
                break

            # Asks user if they want to see more items
            user_ans = self.request_more(30 - shown_posts)
            if not user_ans:
                break
            to_show = user_ans


def get_post_count(available_posts):
    """
    Ask user how many posts they would like to view. Pass input to
    validate_count() and return count once validated. If number is 0, ask user
    if they want to exit program.

    Args:
    available_posts: Amount of posts available to be displayed.

    Returns:
    Amount of posts the user wishes to see.
    """

    while True:
        user_input = input(
            f"\nHow many posts do you want to see? ({available_posts} available, or enter 0 to exit.):\n")

        try:
            if validate_count(user_input, available_posts):
                count = int(user_input)
                if count == 0:
                    confirm_exit(count)
                return count

            if available_posts == 1:
                print("\nOnly 1 post left to show.")
                continue

            print(f"\nPlease enter a number between 1 and {available_posts}.")
        except ValueError:
            print("\nPlease enter a number.")


def get_posts(post_choice):
    """
    Instantiate Posts class & instantiate Printer class using Posts instantiation.

    Args:
    post_choice: The post type that the user wishes to view.

    Returns:
    Instantiated Printer class.
    """

    if post_choice == "trending":
        posts = Posts(TRENDING_URL)
    else:
        posts = Posts(NEWEST_URL)

    printer = Printer(posts.get_info())
    return printer


def view_posts(post_choice):
    """
    Return requested posts using user's post choice. Check for bad HTTP request
    or invalid Beautiful Soup class.

    Args:
    post_choice: The post type that the user wishes to view.

    Returns:
    User's requested posts.
    """

    try:
        printer = get_posts(post_choice)
    except Exception as e:
        print("\nThe program has encountered a runtime error. Please run the program again, or try selecting alternate posts.")
        print("This error may be caused by a change to Hacker News.")
        print(f"\nerror: '{e}'")
        sys.exit()

    return printer.print_info(get_post_count(30))


def view_more(post_choice):
    """
    Ask user if they want to view alternate posts to the ones they have already
    viewed and display them if so.

    Args:
    post_choice: The post type that the user wishes to view.

    Returns:
    Alternate posts to the ones the user has already viewed.
    """

    if post_choice == "trending":
        to_view = "newest"
    else:
        to_view = "trending"

    user_input = validate_choice(
        f"\nWould you like to see the {to_view} posts now? (yes / no):\n", "yes", "no")
    if user_input == "yes":
        view_posts(to_view)


def confirm_exit(num):
    """
    Check if user input is 0 and, if so, ask user if they wish to exit the
    program.

    Args:
    num: User input from get_post_count().
    """

    if num == 0:
        user_ans = validate_choice(
            "\nDo you want to exit the program? (yes / no):\n", "yes", "no")
        if user_ans == "yes":
            print("\nThank you for using the Hacker News Web Scraper!")
            sys.exit()


def main():
    """Handle greeting the user, calling all functions and running the
    application."""

    print(
        "\nWelcome to the Hacker News Web Scraper! This tool allows you to view\n"
        "the latest posts from Y Combinator's popular technology news site.\n")

    post_choice = validate_choice(
        "What type of posts do you want to see? (trending / newest):\n", "trending", "newest")

    view_posts(post_choice)

    view_more(post_choice)

    print("\nThank you for using the Hacker News Web Scraper!")


if __name__ == "__main__":
    main()
