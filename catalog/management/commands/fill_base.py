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
            {'name': 'Другое', 'description': ''},
            {'name': 'Серверное оборудование', 'description': 'Серверы и серверное оборудование'}
        ]

        fill_categories = []
        for category in categories_list:
            fill_categories.append(Category(**category))

        Category.objects.all().bulk_create(fill_categories)

        # Лист с продуктами
        products_list = [
            {'name': 'Light', 'description': '- Ежемесячное обновление', 'category_id': 1, 'price_item': 599,
             'is_published': True},
            {'name': 'Medium', 'description': '- Поддержка \n- Ежемесячное обновление', 'category_id': 1,
             'price_item': 1499, 'is_published': True},
            {'name': 'TOP', 'description': '- Поддержка \n- Установка на сервер\n- Ежемесячное обновление',
             'category_id': 1, 'price_item': 2599, 'is_published': True},
            {'name': 'Fix soft', 'description': 'Восстановление ПО без подписки', 'category_id': 2, 'price_item': 4599,
             'is_published': False},
            {'name': 'Серверная платформа Supermicro SYS-6029P-WTR',
             'description': 'Серверная платформа SYS-6029P-WTR предназначена для монтирования в стойку формата 2U. '
                            'Поддерживает линейку процессоров Intel Xeon Scalable.',
             'category_id': 3,
             'price_item': 223820,
             'image': '/catalog/1003010.jpg',
             'is_published': True},
            {'name': 'Серверная платформа SuperMicro SYS-5019P-WTR',
             'description': 'Серверная платформа SYS-5019P-WTR для монтажа в стойку высотой 1U. '
                            'В ее основе находится материнская плата Super X11SPW-TF. '
                            'Используется в малых и средних офисах.',
             'category_id': 3,
             'price_item': 219810,
             'image': '/catalog/1003002.jpg',
             'is_published': True},
            {'name': 'Блок питания HP 865408-B21 500W Flex',
             'description': 'блок питания мощностью 500Вт, Hot-Plug, энегоэффективность: 96%, '
                            'входное напряжение: 200 - 277V AC, 380V DC, для HPE ProLiant Gen10 и 300 серии Gen9, '
                            '680x40x225мм',
             'category_id': 3,
             'price_item': 15140,
             'image': '/catalog/998539.jpg',
             'is_published': True},
            {'name': 'Жесткий диск 600Gb SAS Seagate Cheetah 15K.7',
             'description': '600 Гб, SAS, форм фактор 3.5", 15000 об/мин, 16 Мб',
             'category_id': 3,
             'price_item': 28020,
             'image': '/catalog/943251.jpg',
             'is_published': False},
            {'name': 'Вентилятор SuperMicro FAN-0065L4',
             'description': 'вентилятор для серверных корпусов, 40x40 мм, 13000 об/мин, PWM, 4-pin',
             'category_id': 3,
             'price_item': 5570,
             'image': '/catalog/940009.jpg',
             'is_published': True}
        ]

        fill_products = []
        for product in products_list:
            fill_products.append(Product(**product))

        Product.objects.all().bulk_create(fill_products)
