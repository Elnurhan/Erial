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
        for i, v in self.data.items():
            News.objects.create(
                title=i,
                link=v,
                site='Rambler'
            )


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
        for i, v in self.data.items():
            News.objects.create(
                title=i,
                link=v,
                site='Ria'
            )

class LentaController(object):
    '''
    Данный класс предназначен для сохранения данных в БД.
    Функция save_parsed_data сначала чистит БД, а затем добавляет
    в неё новые данные.
    '''
    def __init__(self, data):
        super(LentaController, self).__init__()
        self.data = data

    def save_parsed_data(self):
        for i, v in self.data.items():
            News.objects.create(
                title=i,
                link=v,
                site='Lenta'
            )


class RegnumController(object):
    '''
    Данный класс предназначен для сохранения данных в БД.
    Функция save_parsed_data сначала чистит БД, а затем добавляет
    в неё новые данные.
    '''
    def __init__(self, data):
        super(RegnumController, self).__init__()
        self.data = data
        print(self.data)

    def save_parsed_data(self):
        for i, v in self.data.items():
            News.objects.create(
                title=i,
                link=v,
                site='Regnum'
            )