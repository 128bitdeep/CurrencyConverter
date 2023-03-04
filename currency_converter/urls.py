from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('result/', views.result, name='result'),
    path('invalid_input/', views.invalid_input, name='invalid_input'),
]
