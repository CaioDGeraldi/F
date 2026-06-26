from django.urls import path
from . import views

app_name = 'whatsapp'

urlpatterns = [
    path('', views.index, name='index'),
]