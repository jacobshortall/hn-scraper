import requests
from bs4 import BeautifulSoup

trending_response = requests.get("https://news.ycombinator.com/news").text
newest_response = requests.get("https://news.ycombinator.com/newest").text

trending_html = BeautifulSoup(trending_response, "html.parser")
newest_html = BeautifulSoup(newest_response, "html.parser")


class Posts:
    def __init__(self, html):
        self.html = html

    def get_titles(self):
        html_titles = self.html.find_all(class_="storylink")
        return [title.text for title in html_titles]
