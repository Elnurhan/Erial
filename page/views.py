from django.shortcuts import render
from .models import New
from .parsers.parsers import Rambler, Ria
from .parsers.controllers import RamblerController, RiaController

# Create your views here.
def parse():
    # Данная функция парсит данные с помощью парсера,
    # описанного в файле parsers.py. Далее сохраняет в БД,
    # с помощью контроллера, описанного в файле controllers.py
    x = Rambler().main()

    control = RamblerController(x)
    control.save_parsed_data()

    x = Ria().main()

    control = RiaController(x)
    control.save_parsed_data()

def news_list(request):
    news = New.objects.all()
    parse()
    return render(request, 'page/news_list.html', {'news': news})