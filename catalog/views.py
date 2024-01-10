from urllib import request

from django.forms import inlineformset_factory
from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView, ListView, DetailView, CreateView

from catalog.forms import ProductForm
from catalog.models import Category, Product


class IndexView(TemplateView):
    template_name = 'catalog/index.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['object_list'] = Product.objects.all().order_by('?')[:2]
        return context_data


class ContactsView(TemplateView):
    template_name = 'catalog/contacts.html'

    def get_context_data(self, **kwargs):
        if self.request.method == 'POST':
            name = self.request.POST. get('name')
            phone = self.request.POST.get('phone')
            email = self.request.POST.get('email')
            message = self.request.POST.get('message')
            print(f'Пришло сообщение:\nИмя: {name}\nТел.: {phone}\nEmail: {email}\nСообщение: {message}')
        return super().get_context_data(**kwargs)


class CategoryListView(ListView):
    model = Category


class ProductsListView(ListView):
    model = Product

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(category_id=self.kwargs.get('pk'))
        return queryset


class ProductDetailView(DetailView):
    model = Product


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm

    def get_success_url(self):
        return reverse('catalog:products', args=[self.object.category.pk])

    # def get_context_data(self, **kwargs):
    #     context_data = super().get_context_data(**kwargs)
    #     SubjectFormset = inlineformset_factory(Product, Subject, )