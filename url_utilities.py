#mysite/urls.py
#Pointing urls from another app
#Whenever Django encounters include(), it chops off whatever part of the URL matched up to that point and sends the remaining string to the included URLconf for further processing.

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]

#app/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
