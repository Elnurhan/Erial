from django.shortcuts import render
from .models import News
from .parsers.parsers import *
from .parsers.controllers import *

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
    return render(request, 'page/news_list.html', {'news': news})