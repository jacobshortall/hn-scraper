import requests
from bs4 import BeautifulSoup

trending_response = requests.get("https://news.ycombinator.com/news").text
newest_response = requests.get("https://news.ycombinator.com/newest").text

trending_html = BeautifulSoup(trending_response, "html.parser")
newest_html = BeautifulSoup(newest_response, "html.parser")


class Posts:
    def __init__(self, html):
        self.html = html

    def get_info(self):
        """Fetch post data from given HTML and return a list containing a 
        dictionary for each post."""

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

    def request_more(self):
        """Ask user if they want to view more posts and, if so, how many."""

        user_input = validate_choice(
            "Do you want to see more posts? (yes/no):\n", "yes", "no")
        if user_input == "no":
            return False
        return int(input("Amount:\n"))

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

            # Asks user if they want to see more items
            user_ans = self.request_more()
            if not user_ans:
                break
            shown_posts += to_show
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


def validate_count():
    """Get number from 1-30 from user, checking input is valid and returning 
    number if so."""

    while True:
        try:
            count = int(input("How many posts do you want to see?\n"))
            if 1 <= count <= 30:
                return count
            print("Please enter a number between 1 and 30.")
        except ValueError:
            print("Please enter a number.")


xx = Posts(trending_html)
xx.print_info(1)
