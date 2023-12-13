from django.db import models

NULLABLE = {'null': True, 'blank': True}


class Category(models.Model):
    """ Модель для описания категории товара """
    name = models.CharField(max_length=50, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание', **NULLABLE)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Product(models.Model):
    """ Модель для описания товара Product """
    name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание', **NULLABLE)
    image = models.ImageField(upload_to='catalog/', verbose_name='Изображение(превью)', **NULLABLE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    price_item = models.IntegerField(verbose_name='Цена за штуку')
    date_make = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    date_change = models.DateTimeField(auto_now=True, verbose_name='Дата последнего изменения')

    def __str__(self):
        return f'{self.name} ({self.category}, {self.price_item}, {self.date_make}/{self.date_change})'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
