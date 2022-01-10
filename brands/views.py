from django.http import Http404
from django.http import HttpResponse
from django.core import serializers
from .models import Brand


def index(request):
    # Проверяем что бы был GET запрос, иначе 404 ошибка
    if request.method == 'GET':
        # Создам запрос на выборку всех данных из БД
        brands = Brand.objects.all()

        # Если имеется параметр 'name' в запросе
        if 'name' in request.GET:
            # Создаём запрос на фильтрацию всех брендов где имеется в имени часть name
            # SELECT * FROM brands WHERE 'name' LIKE '*****'
            brands = brands.filter(name__contains=request.GET.get('name'))

        # Представляем объекты в JSON формат
        data = serializers.serialize("json", brands, fields=('name', 'description'))

        # Возвращаем JSON ответ пользователю
        return HttpResponse(data, content_type="application/json")
    else:
        return Http404()
