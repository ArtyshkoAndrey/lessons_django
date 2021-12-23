from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('lesson3/', include('lesson3.urls')),

    path('admin/', admin.site.urls),
]
