import requests
from bs4 import BeautifulSoup
from pprint import pprint


class SearchWords:
    def __init__(self, url, words):
        self.url = url
        self.words = words

    def up_articles(self):
        res = requests.get(self.url + '/ru/all')
        text = res.text
        soup = BeautifulSoup(text, features='html.parser')
        articles = soup.find_all('article')

        for article in articles:
            text_article = [t.text.strip() for t in article.find_all('div', class_="article-formatted-body")]
            for i in self.words:
                for l in text_article:
                    if i in l:
                        t = article.find('time')
                        datetime = t.attrs.get('title')
                        heading = article.find('h2').text.strip()
                        a = article.find('a', class_="tm-article-snippet__title-link")
                        link = a.attrs.get('href')
                        print(f'<{datetime}> - <{heading}> - <{self.url}{link}>')
                        # pprint(text_article)


if __name__ == "__main__":
    url = 'https://habr.com'
    KEYWORDS = ['дизайн', 'фото', 'web', 'python', 'хочу', 'браузерами']
    sw = SearchWords(url, KEYWORDS)
    sw.up_articles()


