import requests
from bs4 import BeautifulSoup
from pprint import pprint

# KEYWORDS = ['дизайн', 'фото', 'web', 'Python']
KEYWORDS = ['Матрицы', 'DIY']
URL = 'https://habr.com'


def getting_articles():
    res = requests.get(URL + '/ru/all')
    text = res.text
    soup = BeautifulSoup(text, features='html.parser')
    articles = soup.find_all('article')

    info_list = []
    for link_article in articles:
        a = link_article.find('a', class_="tm-article-snippet__title-link")
        link = URL + a.attrs.get('href')
        res_article = requests.get(link)
        article_str = res_article.text
        bf_soup = BeautifulSoup(article_str, features='html.parser')
        article_info = bf_soup.find_all('article')
        for art in article_info:
            text_article = [t.text.strip() for t in art.find_all('div', class_="article-formatted-body")]
            for i in text_article:
                for word in KEYWORDS:
                    if word in i:
                        time = art.find('time')
                        datetime = time.attrs.get('title')
                        heading = art.find('h1').text.strip()
                        info = f'<{datetime}> - <{heading}> - <{link}>'
                        if info in info_list:
                            pass
                        else:
                            info_list.append(info)

    for l in sorted(info_list):
        print(l)

# 1 ЗАДАНИЕ
#     for article in articles:
#         text_article = [t.text.strip() for t in article.find_all('div', class_="tm-article-snippet")]
#         for i in text_article:
#             for word in KEYWORDS:
#                 if word in i:
#                     time = article.find('time')
#                     datetime = time.attrs.get('title')
#                     heading = article.find('h2').text.strip()
#                     a = article.find('a', class_="tm-article-snippet__title-link")
#                     link = a.attrs.get('href')
#                     info = f'<{datetime}> - <{heading}> - <{URL}{link}>'
#                     info_list.append(info)
#     for l in sorted(list(set(info_list))):
#         print(l)


if __name__ == "__main__":
    getting_articles()
