from django import forms
from catalog.models import Product, Version
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

stop_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']


class CrispyFormMixin(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-exampleForm'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.form_action = 'submit_survey'

        self.helper.add_input(Submit('submit', 'Submit'))


class ProductForm(CrispyFormMixin, forms.ModelForm):
    """ Форма для Product """
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


class VersionForm(CrispyFormMixin, forms.ModelForm):
    """ Форма для Version """
    class Meta:
        model = Version
        fields = '__all__'


class ModeratorProductForm(CrispyFormMixin, forms.ModelForm):
    """ Форма для модератора Product """
    class Meta:
        model = Product
        fields = ('name', 'category', 'image', 'price_item', 'description', 'is_published')
