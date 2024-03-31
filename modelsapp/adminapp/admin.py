from django.contrib import admin
from  modapp.models import Products, Order, User

# Register your models here.

@admin.action(description='Сбросить всё кол-во в ноль')
def reset_quantity(modeladmin, request, queryset):
    queryset.update(quantity=0)

class ProductAdmin(admin.ModelAdmin):
    '''списки продуктов'''
    list_display = ['id', 'name', 'price', 'quantity']
    ordering = ['name', '-quantity']
    list_filter = ['name', 'price', 'description', 'quantity']
    search_filter = ['name', 'price', 'description', 'quantity']
    search_help_text = 'Поиски по описанию продуктов(description)'
    actions = [reset_quantity]

    '''Отдельный продукт'''
    #fields = ['name', 'description', 'quantity', 'price']
    #readonly_fields = ['id', 'name']

class UserAdmin(admin.ModelAdmin):
    '''Список пользователей'''
    list_display = ['id', 'name', 'email', 'phone', 'address', 'date_registered']
    ordering = ['name', 'phone', 'address']
    list_filter = ['name', 'id']
    search_fields = ['name', 'email', 'phone']
    search_help_text = 'Поиски по имени пользователей(name)'

    '''Client'''
    #fields = ['name', 'phone', 'email', 'address', 'country', 'city', 'state', 'date_registered']
    #readonly_fields = ['id', 'name', 'date_registered']

class OrderAdmin(admin.ModelAdmin):
    '''Список заказов'''

    def _products(self, row):
        return ', '.join([str(product) for product in row.products.all()])

    def _customer(self, row):
        return row.customer.username

    list_display = ['customer', '_products', 'total_price', 'date_ordered']
    ordering = ['customer', 'total_price', 'date_ordered']
    list_filter = ['customer', 'total_price', 'date_ordered']
    search_fields = ['customer', 'total_price', 'date_ordered']

    #'''Заказы'''

    #fields = ['customer', 'products', 'total_price', 'date_ordered']
    readonly_fields = ['date_ordered']

fieldsets = [
    (
        None,
        {
            'classes' : ['wide'],
            'fields' : ['name'],
        },
    ),
    (
        'Подробности',
        {
            'classes' : ['collapse'],
            'description' : 'Категория товара и его подробное описание',
            'fields' : ['description', 'customer'],
        },
    ),
    (
        'Бухгалтерия',
        {
            'fields' : ['price', 'quantity'],
        }
    ),
    (
        ' Прочие',
        {
            'description' : 'Рейтинг сформирован автоматически на основе оценок покупателей',
            'fields' : ['date_added'],
        }
    ),
]

admin.site.register(User, UserAdmin)
admin.site.register(Products, ProductAdmin)
admin.site.register(Order, OrderAdmin)