import logging

from django.core.files.storage import FileSystemStorage
from .forms import ProductFormWidget, ProductChoiceForm
from  modapp.models import Products
from django.shortcuts import render
from django.shortcuts import redirect

# Create your views here.

log = logging.getLogger(__name__)

def product_update_form(request, product_id):
    if request.method == 'POST':
        form = ProductFormWidget(request.POST, request.FILES)
        if form.is_valid():
            log.info('Product')
            name = form.cleaned_data['name']
            price = form.cleaned_data['price']
            description = form.cleaned_data['description']
            number = form.cleaned_data['number']

            image = request.FILES['image']
            fs = FileSystemStorage()
            fs.save(image.name, image)

            product = Products.objects.filter(pk=product_id).first()
            product.name = name
            product.price = price
            product.description = description
            product.quantity = number
            product.image = image.name

            product.save()
    else:
        form = ProductFormWidget()
    return render(request, 'formsapp/product_update.html', {'form': form})

def product_update_id_form(request):
    if request.method == 'POST':
        form = ProductChoiceForm(request.POST)
        if form.is_valid():
            log.info(f'Получили {form.cleaned_data=}.')
            product_id = form.cleaned_data['product_id'] # получаем id продукта - номер из списка.
            response = redirect(f'/hw4/product_update/{product_id}')
            return response
    else:
        form = ProductChoiceForm()
    return render(request, 'formsapp/product_update_id.html', {'form': form})

def index(request):
    return render(request, 'formsapp/index.html')


