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

        lines = soup.findAll("a", class_ = "daily__news-item")[:10]
        for text in lines:
            # Удаление символов '\n' и пробелов
            self.news_and_links[re.sub('^\d+\n+|\n+\d+$', ' ', text.text[3::].strip())] = 'https://news.rambler.ru' + text.get("href")

        return self.news_and_links

    def main(self):
        return self.find_news(self.get_html(self.url))


class Ria:
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

        links = soup.findAll("a", class_="cell-list__item-link color-font-hover-only")[:10]

        for text in links:
            self.news_and_links[text.text] = text.get("href")

        return self.news_and_links

    def main(self):
        return self.find_news(self.get_html(self.url))


class Lenta:
    '''
    Данный класс предназначен для парсинга сайта Lenta.
    При инициализации данного класса, устанавливается ссылка на сайт Lenta.
    '''
    def __init__(self):
        '''
        Переменные:
            url = ссылка на страницу, с которой парсим данные.
        '''
        self.url = "https://lenta.ru/"
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

        daily_news = soup.find("div", class_="b-yellow-box__wrap")
        links = daily_news.findAll("a")

        for text in links:
            self.news_and_links[text.text] = "https://lenta.ru/" + text.get("href")

        return self.news_and_links

    def main(self):
        return self.find_news(self.get_html(self.url))


class Regnum:
    '''
    Данный класс предназначен для парсинга сайта Regnum.
    При инициализации данного класса, устанавливается ссылка на сайт Regnum.
    '''
    def __init__(self):
        '''
        Переменные:
            url = ссылка на страницу, с которой парсим данные.
        '''
        self.url = "https://regnum.ru/main.html"
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

        daily_news = soup.find("div", class_="news-container")
        links = daily_news.findAll("a")[:10]

        for text in links:
            self.news_and_links[re.sub(" +", " ", text.text)[20::].replace('\n', '').strip()] = text.get("href").replace("\n","").strip()

        return self.news_and_links

    def main(self):
        return self.find_news(self.get_html(self.url))


class Gazeta:
    '''
    Данный класс предназначен для парсинга сайта Gazeta.
    При инициализации данного класса, устанавливается ссылка на сайт Gazeta.
    '''
    def __init__(self):
        '''
        Переменные:
            url = ссылка на страницу, с которой парсим данные.
        '''
        self.url = "https://www.gazeta.ru/"
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

        lines = soup.find("ul", class_="sausage-list sausage-list-maintheme mb20 maintheme-flow")
        links = lines.findAll('a')[:10]

        for text in links:
            self.news_and_links[text.text.strip()] = "https://www.gazeta.ru" + text.get('href')

        return self.news_and_links

    def main(self):
        return self.find_news(self.get_html(self.url))


class Rg:
    '''
    Данный класс предназначен для парсинга сайта Rg.
    При инициализации данного класса, устанавливается ссылка на сайт Rg.
    '''
    def __init__(self):
        '''
        Переменные:
            url = ссылка на страницу, с которой парсим данные.
        '''
        self.url = "https://rg.ru/"
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

        lines = soup.find('div', class_='b-feed__list')
        links = lines.findAll('a')[:10]

        for text in links:
            self.news_and_links[text.text] = "https://rg.ru" + text.get("href")

        return self.news_and_links

    def main(self):
        return self.find_news(self.get_html(self.url))

