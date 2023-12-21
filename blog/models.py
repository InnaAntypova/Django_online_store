from django.db import models

NULLABLE = {'null': True, 'blank': True}


class Article(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    slug = models.CharField(max_length=150, verbose_name='Slug')
    body = models.TextField(verbose_name='Содержимое')
    image = models.ImageField(upload_to='blog/', **NULLABLE, verbose_name='Превью(изображение)')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    is_published = models.BooleanField(default=True, verbose_name='Признак публикации')
    count_views = models.SmallIntegerField(default=0, verbose_name='Количество просмотров')

    def __str__(self):
        return f"{self.title}({self.is_published}, {self.count_views})"

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
