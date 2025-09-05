from django.urls import path
from .views import lab1

urlpatterns=[
    path('',lab1,name='lab1'),
]