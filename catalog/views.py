from django.shortcuts import render


def index(request):
    return render(request, 'catalog/index.html')


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f'Пришло сообщение:\nИмя: {name}\nТел.: {phone}\nEmail: {email}\nСообщение: {message}')
    return render(request, 'catalog/contacts.html')


