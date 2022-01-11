import json

from django.core import serializers
from django.http import Http404
from django.http import HttpResponse

from . import forms
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


def create(request):
    # Проверяем что бы был POST запрос, иначе 404 ошибка
    if request.method == 'POST':
        # Создаём экземпляр валидатора с POST данными
        form = forms.BrandValidate(request.POST or None)

        # Если данные верны, то создадим новый бренд и вернём ответ
        if form.is_valid():
            form.save()
            data = json.dumps({'save': 'True'})
            return HttpResponse(data, content_type="application/json")

        # Возвращаем JSON ответ об ошибке
        data = json.dumps({'save': 'False'})
        return HttpResponse(data, content_type="application/json")
    else:
        return Http404()


def show(request, id):
    if request.method == 'GET':
        brand = Brand.objects.get(id=id)
        # Сериaлизация данных
        data = serializers.serialize("json", [brand], fields=('name', 'description'))

        # Возвращаем JSON ответ пользователю
        return HttpResponse(data[1:-1], content_type="application/json")
    else:
        return Http404()
