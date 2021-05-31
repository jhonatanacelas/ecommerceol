from django.shortcuts import render
from .models import Shipping
from rest_framework import viewsets
from rest_framework import permissions
from .serializer import ShippingSerializer


class ShippingViewSet(viewsets.ModelViewSet):
    queryset = Shipping.objects.all()
    serializer_class = ShippingSerializer
    permission_classes = [permissions.IsAuthenticated]