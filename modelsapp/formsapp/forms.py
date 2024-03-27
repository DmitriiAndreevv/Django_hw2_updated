import _datetime
from django import forms

from modapp.models import Products

class ProductFormWidget(forms.Form):

    name = forms.CharField(max_length=50, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': f'Введите название товара -'}))
    price = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    number = forms.IntegerField(min_value=1)
    image = forms.ImageField()

class ProductChoiceForm(forms.Form):
    products = Products.objects.all()
    product_id = forms.ChoiceField(label=f'product', choices=[(product.id, product.name) for product in products])

class ImageForm(forms.Form):
    image = forms.ImageField()