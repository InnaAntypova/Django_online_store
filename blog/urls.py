from django.urls import path
from django.views.decorators.cache import never_cache

from blog.views import ArticleListView, ArticleCreateView, ArticleDetailView, ArticleUpdateView, ArticleDeleteView
from blog.apps import BlogConfig

app_name = BlogConfig.name

urlpatterns = [
    path('', ArticleListView.as_view(), name='article_list'),
    path('create/', never_cache(ArticleCreateView.as_view()), name='create_article'),
    path('detail/<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),
    path('update/<int:pk>/', ArticleUpdateView.as_view(), name='article_update'),
    path('delete/<int:pk>/', ArticleDeleteView.as_view(), name='article_delete'),
]
