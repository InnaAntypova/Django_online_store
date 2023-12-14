from django.core.management import BaseCommand
from django.core.management.color import no_style
from django.db import connection

from catalog.models import Product, Category


class Command(BaseCommand):
    def handle(self, *args, **options):
        # Удаляет ранее созданные объекты Category и Product
        Category.objects.all().delete()
        Product.objects.all().delete()

        # Сброс PrimaryKey в таблицах
        sequence_sql = connection.ops.sequence_reset_sql(no_style(), [Category, Product])
        with connection.cursor() as cursor:
            for sql in sequence_sql:
                cursor.execute(sql)

        # Лист с категориями
        categories_list = [
            {'name': 'Подписка', 'description': 'Регулярное обновление и сопровождение ПО согласно тарифа'},
            {'name': 'Другое', 'description': ''}
        ]

        fill_categories = []
        for category in categories_list:
            fill_categories.append(Category(**category))

        Category.objects.all().bulk_create(fill_categories)

        # Лист с продуктами
        products_list = [
            {'name': 'Light', 'description': '- Ежемесячное обновление', 'category_id': 1, 'price_item': 599},
            {'name': 'Medium', 'description': '- Поддержка \n- Ежемесячное обновление', 'category_id': 1,
             'price_item': 1499},
            {'name': 'TOP', 'description': '- Поддержка \n- Установка на сервер\n- Ежемесячное обновление',
             'category_id': 1, 'price_item': 2599},
            {'name': 'Fix soft', 'description': 'Восстановление ПО без подписки', 'category_id': 2, 'price_item': 4599}
        ]

        fill_products = []
        for product in products_list:
            fill_products.append(Product(**product))

        Product.objects.all().bulk_create(fill_products)
