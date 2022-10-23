from rest_framework import serializers

from .models import Customer, Product, Order


class CustomerSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Customer
        fields = [
            'id',
            'firstname',
            'lastname'
        ]
        
class ProductSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Product
        fields = [
            'id',
            'name',
            'cost'
        ]
        
class OrderSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Order
        fields = [
            'id',
            'customer',
            'products'
        ]