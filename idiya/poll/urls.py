from django.urls import path
from . import views
urlpatterns=[
        path('', views.yandex, name='index'),
        ]
