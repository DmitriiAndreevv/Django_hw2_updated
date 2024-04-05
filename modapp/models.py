from django.db import models



class User(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    date_registered = models.DateField(auto_now_add=True)

    def __str__(self):
        return (
            f'client:{self.name}, phone:{self.phone}, email:{self.email},address: {self.address}, country: {self.country},'
            f'city: {self.city}, state: {self.state}')


class Products(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    quantity = models.IntegerField()
    date_added = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='products/')

    def __str__(self):
        return f'product name: {self.name}, price: {self.price}, description: {self.description}, quantity:{self.quantity}'


class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Products)
    date_ordered = models.DateField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'customer: {self.customer.name}, products: {self.products}, date_ordered: {self.date_ordered}, total_price: {self.total_price}'
