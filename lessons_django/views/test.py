from django.http import HttpResponse
from django.shortcuts import render
from lessons_django.decorators import api_view

@api_view(['GET'])
def index(request):
    return HttpResponse('Hello Word')
