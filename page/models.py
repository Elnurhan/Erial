from django.db import models, connection

# Create your models here.
class New(models.Model):
    '''
    Модель новостей.
    Переменные:
        title = заголовок новости.
        link  = ссылка на новость.
        site  = сайт, с которого данная новость была взята
    '''
    title = models.CharField(max_length=150)
    link  = models.CharField(max_length=250)
    site  = models.CharField(max_length=50)

    @classmethod
    def truncate(cls):
        with connection.cursor() as cursor:
            cursor.execute('TRUNCATE TABLE `{0}`'.format(cls._meta.db_table))

    def __str__(self):
        return self.title;