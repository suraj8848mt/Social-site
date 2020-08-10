
from django.contrib import admin
from django.urls import path, include

from api.views.item import ItemList, ItemDetail
from api.views.asset_bundle import AssetBundleList, AssetBundleDetail

app_name= 'item'

urlpatterns = [
    path('items/', ItemList.as_view(), name='item-list'),
    path('items/<int:pk>/', ItemDetail.as_view(), name='item-detail'),
    path('assets/', AssetBundleList.as_view(), name='assets-list'),
    path('assets/<int:pk>/', AssetBundleDetail.as_view(), name='item-detail'),
]
