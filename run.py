import requests
from bs4 import BeautifulSoup
from validation import validate_choice, validate_count, validate_http

trending_url = "https://news.ycombinator.com/news"
newest_url = "https://news.ycombinator.com/newest"


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


def main():
    """Handle greeting the user, calling all functions and running the 
    application. Also handle validating HTTP for required links."""

    print(
        "\nWelcome to the Hacker News Web Scraper! This tool allows you to view the latest posts from Y Combinator's popular technology news site.\n")

    post_choice = validate_choice(
        "What type of posts do you want to see? (trending / newest)\n", "trending", "newest")
    if post_choice == "trending":
        posts = Posts(trending_url)
    else:
        posts = Posts(newest_url)

    posts.print_info(validate_count(30))

    print("\nThank you for using the Hacker News Web Scraper!")


if __name__ == "__main__":
    main()
