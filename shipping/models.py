from django.db import models


class Shipping(models.Model):
    address = models.CharField(max_length=1000,blank=False,null=False)
    updated_at = models.DateTimeField(auto_now=True, verbose_name='actualizado el')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='creado el')

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'shipping'
        verbose_name_plural = 'Shippings'
        db_table = 'shipping'