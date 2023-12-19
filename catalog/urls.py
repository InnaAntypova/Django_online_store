from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import index, contacts, category, products, save_product, product_detail

app_name = CatalogConfig.name

urlpatterns = [
    path('home/', index, name='index'),
    path('contacts/', contacts, name='contacts'),
    path('category/', category, name='category'),
    path('<int:pk>/products/', products, name='products'),
    path('<int:pk>/product_detail/', product_detail, name='product_detail'),
    path('save_product/', save_product, name='save_product')
]
