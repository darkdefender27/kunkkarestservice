from rest_framework import serializers
from meatmarketrestservice.models import Item


class ItemSerializer(serializers.ModelSerializer):

    class Meta(object):
        model = Item
        fields = ('itemId', 'itemName', 'itemDescription', 'itemRate')

    def create(self, validated_data):
        """
        Create and return a new `Item` instance, given the validated data.
        """
        return Item.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Item` instance, given the validated data.
        """
        instance.itemId = validated_data.get('itemId', instance.itemId)
        instance.itemName = validated_data.get('code', instance.itemName)
        instance.itemDescription = validated_data.get('linenos', instance.itemDescription)
        instance.itemRate = validated_data.get('language', instance.itemRate)

        instance.save()
        return instance
