from django_online_store import settings
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from pytils.translit import slugify
from django.core.mail import send_mail
from blog.models import Article


# class SlugBlogMixin:
#     def form_valid(self, form):
#         if form.is_valid():
#             new_article = form.save()
#             new_article.slug = slugify(new_article.title)
#             new_article.save()
#         return super().form_valid(form)


class ArticleListView(ListView):
    model = Article

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)
        return queryset


class ArticleDetailView(DetailView):
    model = Article

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.count_views += 1
        self.object.save()
        if self.object.count_views == 100:
            self.send_article_mail()
        return self.object

    def send_article_mail(self):
        send_mail(
            '!!!Уведомление!!!',
            f"""Поздравляем! Ваша статья "{self.object.title}" набрала 100 просмотров!""",
            settings.EMAIL_HOST_USER,
            [settings.SERVER_EMAIL]
        )


class ArticleCreateView(CreateView):
    model = Article

    fields = ('title', 'body', 'image')
    success_url = reverse_lazy('blog:article_list')

    def form_valid(self, form):
        if form.is_valid():
            new_article = form.save()
            new_article.slug = slugify(new_article.title)
            new_article.save()
        return super().form_valid(form)


class ArticleUpdateView(UpdateView):
    model = Article

    fields = ('title', 'body', 'image', 'is_published')

    def form_valid(self, form):
        if form.is_valid():
            new_article = form.save()
            new_article.slug = slugify(new_article.title)
            new_article.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('blog:article_detail', args=[self.kwargs.get('pk')])


class ArticleDeleteView(DeleteView):
    model = Article

    success_url = reverse_lazy('blog:article_list')

