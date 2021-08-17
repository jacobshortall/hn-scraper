import requests
from bs4 import BeautifulSoup
from validation import validate_choice, validate_count

TRENDING_URL = "https://news.ycombinator.com/news"
NEWEST_URL = "https://news.ycombinator.com/newest"


def get_count(available_posts):
    """Ask user how many posts they would like to view. Pass input to
    validate_count() and return count once validated."""

    while True:
        count = input(
            f"\nHow many posts do you want to see? ({available_posts} available)\n")

        try:
            if validate_count(count, available_posts):
                return int(count)

            if available_posts == 1:
                print("\nOnly 1 post left to show.")
                continue

            print(f"\nPlease enter a number between 1 and {available_posts}.")
        except ValueError:
            print("\nPlease enter a number.")


class Posts:
    def __init__(self, url):
        self.url = url

    def get_info(self):
        """Fetch post data from given HTML and return a list containing a
        dictionary for each post (30 posts total)."""

        response = requests.get(self.url)
        html = BeautifulSoup(response.text, "html.parser")

        html_titles = html.find_all(class_="storylink")
        html_ages = html.find_all(class_="age")

        li = []
        for i in range(30):
            di = {}
            di["title"] = html_titles[i].text
            di["link"] = html_titles[i]["href"]
            di["age"] = html_ages[i].text
            li.append(di)
        return li


class Printer():
    def __init__(self, posts):
        self.posts = posts

    def request_more(self, available_posts):
        """Ask user if they want to view more posts and, if so, how many."""

        user_input = validate_choice(
            "Do you want to see more posts? (yes/no):\n", "yes", "no")
        if user_input == "no":
            return False
        return get_count(available_posts)

    def print_info(self, count):
        """Print initially requested post information to the terminal and ask
        the user if they want to view more posts using request_more function."""

        shown_posts = 0
        to_show = count

        while True:
            for i in self.posts[shown_posts: shown_posts + to_show]:
                print(
                    f"""
                    {self.posts.index(i) + 1}) Title: {i["title"]}
                    Link: {i["link"]}
                    Posted: {i["age"]}
                    """
                )

            shown_posts += to_show
            if shown_posts == 30:
                print("No more posts to show.")
                break

            # Asks user if they want to see more items
            user_ans = self.request_more(30 - shown_posts)
            if not user_ans:
                break
            to_show = user_ans


def main():
    """Handle greeting the user, calling all functions and running the
    application. Also handle validating HTTP for required links."""

    print(
        "\nWelcome to the Hacker News Web Scraper! This tool allows you to view\n"
        "the latest posts from Y Combinator's popular technology news site.\n")

    post_choice = validate_choice(
        "What type of posts do you want to see? (trending / newest)\n", "trending", "newest")
    if post_choice == "trending":
        posts = Posts(TRENDING_URL)
    else:
        posts = Posts(NEWEST_URL)

    printer = Printer(posts.get_info())
    printer.print_info(get_count(30))

    print("\nThank you for using the Hacker News Web Scraper!")


if __name__ == "__main__":
    main()
