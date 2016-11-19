from django.db import models


class Item(models.Model):

    itemId = models.IntegerField(default=0)
    itemName = models.CharField(max_length=25, default="ITEM NAME")
    itemDescription = models.CharField(max_length=100, default="ITEM DESC")
    itemRate = models.IntegerField(default=0)
