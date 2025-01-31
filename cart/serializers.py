from rest_framework import serializers
from .cart import Cart


class CartItemSerializer(serializers.Serializer):
    product = serializers.PrimaryKeyRelatedField(read_only=True)
    price = serializers.DecimalField(
        max_digits=10, decimal_places=2, coerce_to_string=True)
    quantity = serializers.IntegerField()
    total_price = serializers.DecimalField(
        max_digits=10, decimal_places=2, coerce_to_string=True)


class CartSerializer(serializers.Serializer):
    items = CartItemSerializer(many=True, source='__iter__')
    total_price = serializers.DecimalField(
        max_digits=10, decimal_places=2, coerce_to_string=True)

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['total_price'] = str(instance.get_total_price())
        return representation
