from django.contrib import admin
from django.urls import path

from lessons_django.views import test

urlpatterns = [
    path('test', test.index),
    path('admin/', admin.site.urls),
]
