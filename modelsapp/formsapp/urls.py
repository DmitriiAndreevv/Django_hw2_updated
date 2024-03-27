from django.urls import path
from .views import index, product_update_form, product_update_id_form

urlpatterns = [
    path('', index, name='index'),
    path('index/', index, name='index'),
    # path('product_update/', product_update_form, name='product_update'),
    path('product_update/<int:product_id>', product_update_form, name='product_update'),
    path('product_update_id/<int:product_id>', product_update_id_form, name='product_update_id'),


]