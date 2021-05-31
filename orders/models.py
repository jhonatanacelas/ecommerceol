from django.db import models
from users.models import User


class Product(models.Model):
    name = models.CharField(max_length=500, null=False, blank=False, default='')
    value = models.IntegerField(null=False, blank=False)
    is_active = models.BooleanField(default=True, null=False, blank=False)

    updated_at = models.DateTimeField(auto_now=True, verbose_name='actualizado el')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='creado el')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        db_table = 'product'


class Order(models.Model):
    user = models.ForeignKey(User, related_name='orders', on_delete=models.PROTECT)

    updated_at = models.DateTimeField(auto_now=True, verbose_name='actualizado el')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='creado el')

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'
        db_table = 'order'


class Item(models.Model):
    product = models.ForeignKey(Product, related_name='product', on_delete=models.PROTECT)
    order = models.ForeignKey(Order, related_name='items', on_delete=models.PROTECT)
    quantity = models.IntegerField(null=False, blank=False)

    updated_at = models.DateTimeField(auto_now=True, verbose_name='actualizado el')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='creado el')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Items'
        db_table = 'item'
