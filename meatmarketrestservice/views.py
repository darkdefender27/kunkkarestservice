from rest_framework import generics

from meatmarketrestservice.models import Item
from meatmarketrestservice.serializers import ItemSerializer


class ItemList(generics.ListCreateAPIView):
    """
    List all items or create a new item
    """
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class ItemDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete an item
    """
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
