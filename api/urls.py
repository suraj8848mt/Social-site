
from django.contrib import admin
from django.urls import path, include

from .views import ItemList, ItemDetail

app_name= 'item'

urlpatterns = [
    path('items/', ItemList.as_view(), name='item-list'),
    path('items/<int:pk>/', ItemDetail.as_view(), name='item-detail'),
]
