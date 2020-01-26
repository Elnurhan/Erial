from django.shortcuts import render
from .models import News
from .parsers.parsers import *
from .parsers.categories.politic_parser import *
from .parsers.controllers import *

# Create your views here.
def parse():
    '''
    Данная функция парсит данные с помощью парсера,
    описанного в файле parsers.py. Далее сохраняет в БД,
    с помощью контроллера, описанного в файле controllers.py
    '''
    x = Rambler().main()
    control = RamblerController(x)
    control.save_parsed_data()

    x = Ria().main()
    control = RiaController(x)
    control.save_parsed_data()

    x = Lenta().main()
    control = LentaController(x)
    control.save_parsed_data()

    x = Regnum().main()
    control = RegnumController(x)
    control.save_parsed_data()

    x = Gazeta().main()
    control = GazetaController(x)
    control.save_parsed_data()

    x = Rg().main()
    control = RgController(x)
    control.save_parsed_data()

def news_list(request):
    news = News.objects.all()
    parse()
    return render(request, 'page/base.html', {'news': news})

def parse_politic_category():
    x = RamblerPolitics().main()
    control = RamblerController(x)
    control.save_parsed_data()

    x = RiaPolitics().main()
    control = RiaController(x)
    control.save_parsed_data()

    x = RegnumPolitics().main()
    control = RegnumController(x)
    control.save_parsed_data()

    x = RgPolitics().main()
    control = RgController(x)
    control.save_parsed_data()

    x = LentaPolitics().main()
    control = LentaController(x)
    control.save_parsed_data()

    x = GazetaPolitics().main()
    control = GazetaController(x)
    control.save_parsed_data()

def politic_category(request):
    politic_news = News.objects.all()
    parse_politic_category()
    return render(request, 'page/category_politic.html', {'politic_news': politic_news})