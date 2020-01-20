from ..models import News
from django.db import connection


class RamblerController(object):
    '''
    Данный класс предназначен для сохранения данных в БД.
    Функция save_parsed_data сначала чистит БД, а затем добавляет
    в неё новые данные.
    '''
    def __init__(self, data):
        super(RamblerController, self).__init__()
        self.data = data

    def save_parsed_data(self):
        News.truncate()
        print(self.data)
        # Завёл счётчик итераций k, чтобы сохранить первые 10 эл-ов
        # в БД (ничего умнее не нашёл).
        k = 0
        for i, v in self.data.items():
            News.objects.create(
                title=i,
                link=v,
                site='Rambler'
            )
            k += 1
            if k > 9:
                break


class RiaController(object):
    '''
    Данный класс предназначен для сохранения данных в БД.
    Функция save_parsed_data сначала чистит БД, а затем добавляет
    в неё новые данные.
    '''
    def __init__(self, data):
        super(RiaController, self).__init__()
        self.data = data

    def save_parsed_data(self):
        print(len(self.data))
        # Завёл счётчик итераций k, чтобы сохранить первые 10 эл-ов
        # в БД (ничего умнее не нашёл).
        k = 0
        for i, v in self.data.items():
            News.objects.create(
                title=i,
                link=v,
                site='Ria'
            )
            k += 1
            if k > 9:
                break