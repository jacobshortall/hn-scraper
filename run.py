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

    def print_info(self, count):
        info = self.get_info()
        for i in range(count):
            print(
                f"""
                {i+1}) Title: {info[i]["title"]}
                Link: {info[i]["link"]}
                Posted: {info[i]["age"]}
                """
            )


xx = Posts(trending_html)
xx.print_info(3)
