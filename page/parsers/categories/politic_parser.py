import re
import requests
from bs4 import BeautifulSoup

'''
Парсер новостей.
Категория: Политика
'''

class RamblerPolitics:
    def __init__(self):
        '''
        Переменные:
            url = ссылка на страницу, с которой парсим данные.
        '''
        self.url = "https://news.rambler.ru/politics/"
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

        lines = soup.findAll('a', class_='top-card')[:10]

        for text in lines:
            self.news_and_links[re.sub('^\d+\n+|\n+\d+$', ' ', text.text[3::].strip())] = 'https://news.rambler.ru' + text.get("href")

        return self.news_and_links

    def main(self):
        return self.find_news(self.get_html(self.url))


class RiaPolitics:
    def __init__(self):
        '''
        Переменные:
            url = ссылка на страницу, с которой парсим данные.
        '''
        self.url = "https://ria.ru/politics/"
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
        
        lines = soup.findAll('a', class_='list-item__title color-font-hover-only')[:10]

        for text in lines:
            self.news_and_links[text.text] = text.get("href")

        return self.news_and_links

    def main(self):
        return self.find_news(self.get_html(self.url))


class RegnumPolitics:
    def __init__(self):
        '''
        Переменные:
            url = ссылка на страницу, с которой парсим данные.
        '''
        self.url = "https://regnum.ru/news/polit.html"
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

        lines = soup.findAll('a', class_='news-container-item news-container-item--federal')[:10]

        for text in lines:
            self.news_and_links[re.sub(" +", " ", text.text)[21::].replace('\n', '').strip()] = text.get("href").replace("\n","").strip()

        return self.news_and_links

    def main(self):
        return self.find_news(self.get_html(self.url))


class LentaPolitics:
    def __init__(self):
        '''
        Переменные:
            url = ссылка на страницу, с которой парсим данные.
        '''
        self.url = "https://lenta.ru/rubrics/russia/politic/"
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

        lines = soup.find('div', class_='b-tag-page')
        links = lines.findAll('a')[:12]

        for text in links:
            self.news_and_links[text.text] = "https://lenta.ru" + text.get("href")

        # В словаре были пустые ключи, пожтому я их удалил
        self.news_and_links.pop('')

        return self.news_and_links

    def main(self):
        return self.find_news(self.get_html(self.url))


class RgPolitics:
    def __init__(self):
        '''
        Переменные:
            url = ссылка на страницу, с которой парсим данные.
        '''
        self.url = "https://rg.ru/tema/gos/"
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

        # Первые 25 новостей не о политике 
        lines = soup.findAll('a', class_='b-link b-link_title')[26:36]

        for text in lines:
            self.news_and_links[text.text] = text.get("href")

        return self.news_and_links

    def main(self):
        return self.find_news(self.get_html(self.url))


class GazetaPolitics:
    def __init__(self):
        '''
        Переменные:
            url = ссылка на страницу, с которой парсим данные.
        '''
        self.url = "https://www.gazeta.ru/politics/"
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

        print('succ')
        lines = soup.find('div', id='news_lenta_intro')
        links = lines.findAll('a')[1:11]

        for text in links:
            self.news_and_links[text.text.strip()[10::]] = 'https://www.gazeta.ru' + text.get("href")
            
        return self.news_and_links

    def main(self):
        return self.find_news(self.get_html(self.url))

