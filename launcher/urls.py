from django.urls import path
from . import views

app_name = 'launcher'

urlpatterns = [
    path('', views.index, name='index'),
]