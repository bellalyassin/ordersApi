from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.

from .serializers import OrderSerializer
from .models import Orders


class OrdersViewSet(viewsets.ModelViewSet):
    queryset = Orders.objects.all().order_by('dateOrder')
    serializer_class = OrderSerializer
