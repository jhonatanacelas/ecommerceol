from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework import permissions
from .models import Product, Order, Item
from .serializers import ProductSerializer, OrderSerializer, ItemSerializer
from .pagination import ShortResultsSetPagination
from rest_framework.decorators import action
from rest_framework.response import Response
from .tasks import schedule_shipping


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]



class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = ShortResultsSetPagination


    @action(detail=True, methods=['post'])
    def schedule_shipment(self, request, pk=None):
        order = self.get_object()
        schedule_shipping.delay(order.pk)
        return Response(
            {'status': 'Scheduled delivery'},
            status=status.HTTP_400_BAD_REQUEST)




class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [permissions.IsAuthenticated]