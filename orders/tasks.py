from celery import shared_task
from shipping.models import Shipping


@shared_task
def schedule_shipping(order):
    shipping = Shipping(address='address for order ' + str(order))
    shipping.save()
    print('Shipping')