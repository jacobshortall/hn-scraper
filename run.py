import requests
from bs4 import BeautifulSoup

# Preparing and parsing html data using bs4 for use with Posts class
trending_response = requests.get("https://news.ycombinator.com/news").text
newest_response = requests.get("https://news.ycombinator.com/newest").text
trending_html = BeautifulSoup(trending_response, "html.parser")
newest_html = BeautifulSoup(newest_response, "html.parser")


class Posts:
    def __init__(self, html):
        self.html = html

    def get_info(self):
        """Fetch post data from given HTML and return a list containing a 
        dictionary for each post (30 posts total)."""

        html_titles = self.html.find_all(class_="storylink")
        html_ages = self.html.find_all(class_="age")

        li = []
        for i in range(30):
            di = {}
            di["title"] = html_titles[i].text
            di["link"] = html_titles[i]["href"]
            di["age"] = html_ages[i].text
            li.append(di)
        return li

    def request_more(self, available_posts):
        """Ask user if they want to view more posts and, if so, how many."""

        user_input = validate_choice(
            "Do you want to see more posts? (yes/no):\n", "yes", "no")
        if user_input == "no":
            return False
        return validate_count(available_posts)

    def print_info(self, count):
        """Print initially requested post information to the terminal and ask 
        the user if they want to view more posts using request_more function."""

        info = self.get_info()
        shown_posts = 0
        to_show = count

        while True:
            for i in info[shown_posts: shown_posts + to_show]:
                print(
                    f"""
                    {info.index(i) + 1}) Title: {i["title"]}
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


def validate_choice(prompt, option_1, option_2):
    """Validate user input for a question with 2 possible answers, alerting 
    them if input is somehow invalid."""

    while True:
        user_input = input(prompt)
        if user_input == option_1 or user_input == option_2:
            return user_input
        else:
            print(
                "Invalid input! Please make sure all input is correct and in lowercase.\n")


def validate_count(available_posts):
    """Get positive number from user, checking input is below maximum available 
    posts and returning number if so."""

    while True:
        try:
            count = int(
                input(f"How many posts do you want to see? ({available_posts} available)\n"))
            if 1 <= count <= available_posts:
                return count

            if available_posts == 1:
                print("Only 1 post left to show.")
                continue

            print(f"Please enter a number between 1 and {available_posts}.")
        except ValueError:
            print("\nPlease enter a number.\n")


def main():
    """Handle greeting the user, calling all functions and running the 
    application."""

    print(
        "Welcome to the Hacker News Web Scraper! This tool allows you to view the latest posts from Y Combinator's popular technology news site.\n")

    post_type = validate_choice(
        "What posts do you want to see? (trending/newest)\n", "trending", "newest")
    if post_type == "trending":
        posts = Posts(trending_html)
    else:
        posts = Posts(newest_html)

    posts.print_info(validate_count(30))


if __name__ == "__main__":
    main()
