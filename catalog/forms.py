from django import forms

from catalog.models import Product

stop_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('name', 'category', 'image', 'price_item', 'description')

    def clean_name(self):
        cleaned_data = self.cleaned_data.get('name')
        for word in stop_words:
            if word in cleaned_data.lower():
                raise forms.ValidationError('Используется запрещенное название продукта')
        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data.get('description')
        for word in stop_words:
            if word in cleaned_data.lower():
                raise forms.ValidationError('Используется запрещенное слово в описании продукта')
        return cleaned_data
