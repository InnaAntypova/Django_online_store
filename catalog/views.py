from urllib import request

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.forms import inlineformset_factory
from django.http import Http404
from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView

from catalog.forms import ProductForm, VersionForm, ModeratorProductForm
from catalog.models import Category, Product, Version


class IndexView(TemplateView):
    template_name = 'catalog/index.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        # context_data['object_list'] = Product.objects.all().order_by('?')[:2]
        context_data['object_list'] = Product.objects.filter(is_published=True).order_by('?')[:2]
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


class ProductsListView(LoginRequiredMixin, ListView):
    model = Product

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(category_id=self.kwargs.get('pk'))
        queryset = queryset.filter(is_published=True)
        return queryset


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product


    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        data = context_data['object']
        active_version = data.prod_name.filter(is_active=True)
        if active_version:
            for item in active_version:
                data.version_number = item.version_number
                data.version_name = item.version_name
                context_data['version'] = f'{data.version_number} / {data.version_name}'
        else:
            context_data['version'] = ''
        # print(context_data)
        return context_data


class ProductCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Product
    # form_class = ProductForm
    permission_required = 'catalog.add_product'
    permission_denied_message = 'Доступ запрещен.'

    def form_valid(self, form):
        if form.is_valid():
            self.object = form.save()
            self.object.user_create = self.request.user
            self.object.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('catalog:products', args=[self.object.category.pk])

    def get_form_class(self):
        if self.request.user.is_staff or self.request.user.is_superuser:
            return ModeratorProductForm
        return ProductForm


class ProductUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    permission_required = 'catalog.change_product'
    permission_denied_message = 'Доступ запрещен.'

    def get_success_url(self):
        return reverse('catalog:products', args=[self.object.category.pk])

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = VersionFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = VersionFormset(instance=self.object)
        return context_data

    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        self.object = form.save()
        if self.object.user_create == self.request.user:
            self.object.user_create = self.request.user
        self.object.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()
        return super().form_valid(form)

    def get_object(self, *args, **kwargs):
        product = super().get_object(*args, **kwargs)
        if product.user_create == self.request.user or self.request.user.is_superuser or self.request.user.is_staff:
            return product
        return reverse('catalog:products')

    def get_form_class(self):
        if self.request.user.is_staff or self.request.user.is_superuser:
            return ModeratorProductForm
        return ProductForm


class PersonalAreaView(LoginRequiredMixin, PermissionRequiredMixin, TemplateView):
    template_name = 'catalog/personal_area.html'
    permission_required = [
        'catalog.add_product',
        'catalog.change_product']
    permission_denied_message = 'Доступ запрещен.'


class ModeratorProductsView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Product
    permission_required = [
        'catalog.add_product',
        'catalog.change_product']
    permission_denied_message = 'Доступ запрещен.'

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_staff or self.request.user.is_superuser:
            return queryset.all()

        # для пользователя с повышенными правами(не модератор/не админ)
        products = Product.objects.filter(user_create=self.request.user)
        queryset = products
        return queryset
