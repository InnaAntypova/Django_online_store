from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from blog.models import Article


class ArticleListView(ListView):
    model = Article


class ArticleCreateView(CreateView):
    model = Article

    fields = ('title', 'body', 'image')
    success_url = reverse_lazy('blog:article_list')


class ArticleDetailView(DetailView):
    model = Article


class ArticleUpdateView(UpdateView):
    model = Article

    fields = ('title', 'body', 'image')
    success_url = reverse_lazy('blog:article_list')


class ArticleDeleteView(DeleteView):
    model = Article

    success_url = reverse_lazy('blog:article_list')

