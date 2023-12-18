from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import index, contacts, category, products, save_product

app_name = CatalogConfig.name

urlpatterns = [
    path('home/', index, name='index'),
    path('contacts/', contacts, name='contacts'),
    path('category/', category, name='category'),
    path('<int:pk>/products/', products, name='products'),
    path('save_product/', save_product, name='save_product')
]
