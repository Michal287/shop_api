from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=32)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField()
    quantity = models.IntegerField()
    price = models.FloatField(null=False)

    def __str__(self):
        return self.name


class Image(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(blank=True)

    def __str__(self):
        return self.product.name


class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} - {self.product.name}'


class Order(models.Model):
    order_status = (
        ('New order', 'New order'),
        ('Waiting for payment', 'Waiting for payment'),
        ('Paid', 'Paid'),
        ('Preparing the order', 'Preparing the order'),
        ('Waiting for Waybill', 'Waiting for Waybill'),
        ('Waiting for the courier', 'Waiting for the courier'),
        ('Sent', 'Sent'),
        ('Cancel', 'Cancel')
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=64, choices=order_status, default="New order")
    product = models.ManyToManyField(Product)