from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import IndexView, ContactsView, CategoryListView, \
    ProductsListView, ProductDetailView, ProductCreateView, ProductUpdateView

app_name = CatalogConfig.name

urlpatterns = [
    path('home/', IndexView.as_view(), name='index'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('category/', CategoryListView.as_view(), name='category'),
    path('<int:pk>/products/', ProductsListView.as_view(), name='products'),
    path('<int:pk>/product_detail/', ProductDetailView.as_view(), name='product_detail'),
    path('save_product/', ProductCreateView.as_view(), name='save_product'),
    path('<int:pk>/edit_product/', ProductUpdateView.as_view(), name='update_product')
]
