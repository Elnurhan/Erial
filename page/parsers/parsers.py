'''

Реализация парсеров различных новостных сайтов

'''

import re
import requests
from bs4 import BeautifulSoup


class Rambler:
    '''
    Данный класс предназначен для парсинга сайта Rambler.
    При инициализации данного класса, устанавливается ссылка на сайт Rambler.
    '''
    def __init__(self):
        '''
        Переменные:
            url = ссылка на страницу, с которой парсим данные.
        '''
        self.url = "https://news.rambler.ru/"
        self.news_and_links = {}

    def get_html(self, site):
        '''
        Данная функция принимает на вход ссылку на сайт и возвращает
        html-код данного сайта.
        Параметры:
            site = сайт, html-код которого мы хотим получить.
        Возвращает:
            r = html-код данного сайта
        '''
        r = requests.get(site)
        return r.text

    def find_news(self, html):
        '''
        Данная функция принимает на вход html-код и ищет необходимые данные
        с сайта.
        Параметры:
            html = html-код сайта, с которого мы собираемся парсить данные
        Возвращает:
            news_and_links = словарь, в котором ключи - это новости,
            а значения - это ссылки на новость, к которой данный клю привязан
        '''
        soup = BeautifulSoup(html, 'lxml')

        lines = soup.findAll("a", class_ = "daily__news-item")

        for text in lines:
            # Удаление символов '\n' и пробелов
            self.news_and_links[re.sub('^\d+\n+|\n+\d+$', ' ', text.text[3::].strip())] = 'https://news.rambler.ru' + text.get("href")

        return self.news_and_links

    def main(self):
        return self.find_news(self.get_html(self.url))


class Ria(object):
    '''
    Данный класс предназначен для парсинга сайта Ria.
    При инициализации данного класса, устанавливается ссылка на сайт Ria.
    '''
    def __init__(self):
        '''
        Переменные:
            url = ссылка на страницу, с которой парсим данные.
        '''
        self.url = "https://ria.ru/"
        self.news_and_links = {}

    def get_html(self, site):
        '''
        Данная функция принимает на вход ссылку на сайт и возвращает
        html-код данного сайта.
        Параметры:
            site = сайт, html-код которого мы хотим получить.
        Возвращает:
            r = html-код данного сайта
        '''
        r = requests.get(site)
        return r.text

    def find_news(self, html):
        '''
        Данная функция принимает на вход html-код и ищет необходимые данные
        с сайта.
        Параметры:
            html = html-код сайта, с которого мы собираемся парсить данные
        Возвращает:
            news_and_links = словарь, в котором ключи - это новости,
            а значения - это ссылки на новость, к которой данный клю привязан
        '''
        soup = BeautifulSoup(html, 'lxml')

        links = soup.findAll("a", class_="cell-list__item-link color-font-hover-only")
        for text in links:
            self.news_and_links[text.text] = text.get("href")

        return self.news_and_links

    def main(self):
        return self.find_news(self.get_html(self.url))
