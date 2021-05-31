from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Order

class OrderTests(APITestCase):
    def test_create_order(self):
        """
        Ensure we can create a new account object.
        """
        data = {'user': 1}
        response = self.client.post('/orders', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Order.objects.count(), 1)
