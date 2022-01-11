from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:id>/show/', views.show, name='show'),
    path('update/<int:id>/', views.update, name='update'),
    path('<int:id>/', views.delete, name='delete')
]
