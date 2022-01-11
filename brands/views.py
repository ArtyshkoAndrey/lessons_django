import json

from django.core import serializers
from django.http import Http404
from django.http import HttpResponse, JsonResponse

from products.models import Product
from . import forms
from .models import Brand
from .serialiers import BrandSerializer


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
        brand.products.add(Product.objects.first())
        # Сериaлизация данных
        brand_serializer = BrandSerializer(instance=brand)

        # Возвращаем JSON ответ пользователю
        return JsonResponse(brand_serializer.data)
    else:
        return Http404()


def update(request, id):
    # Проверяем что бы был POST запрос, иначе 404 ошибка
    if request.method == 'POST':
        # Создаём экземпляр валидатора с POST данными
        brand = Brand.objects.get(id=id)
        form = forms.BrandValidate(request.POST or None, instance=brand)

        # Если данные верны, то обновим бренд и вернём ответ
        if form.is_valid():
            form.save()
            data = json.dumps({'save': 'True'})
            return HttpResponse(data, content_type="application/json")

        # Возвращаем JSON ответ об ошибке
        data = json.dumps({'save': 'False'})
        return HttpResponse(data, content_type="application/json")
    else:
        return Http404()


def delete(request, id):
    # Проверяем что бы был POST запрос, иначе 404 ошибка
    if request.method == 'DELETE':
        # Создаём экземпляр валидатора с POST данными
        brand = Brand.objects.get(id=id)
        brand.delete()
        data = json.dumps({'save': 'True'})
        return HttpResponse(data, content_type="application/json")
    else:
        return Http404()