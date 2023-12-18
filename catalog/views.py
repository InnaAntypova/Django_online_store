from django.shortcuts import render

from catalog.models import Category, Product


def index(request):
    context = {
        'object_list': Product.objects.all().order_by('?')[:3],
    }
    return render(request, 'catalog/index.html', context)


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f'Пришло сообщение:\nИмя: {name}\nТел.: {phone}\nEmail: {email}\nСообщение: {message}')
    return render(request, 'catalog/contacts.html')


def category(request):
    context = {
        'object_list': Category.objects.all(),
    }
    return render(request, 'catalog/category.html', context)


def products(request, pk):
    context = {
        'object_list': Product.objects.filter(category_id=pk),
    }
    return render(request, 'catalog/products.html', context)


def save_product(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        category_id = request.POST.get('category')
        image = request.POST.get('image')
        price_item = request.POST.get('price_item')
        description = request.POST.get('description')

        product = {'name': name,
                   'description': description,
                   'category_id': category_id,
                   'price_item': price_item,
                   'image': image}
        Product.objects.all().create(**product)

    return render(request, 'catalog/save_product.html')
