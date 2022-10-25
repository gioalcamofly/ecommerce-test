from attr import fields
from rest_framework import serializers

from django.core.validators import FileExtensionValidator

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
        
class UploadReportSerializer(serializers.Serializer):
    
    customers = serializers.FileField(validators=[FileExtensionValidator(allowed_extensions=['csv'])])
    products = serializers.FileField(validators=[FileExtensionValidator(allowed_extensions=['csv'])])
    orders = serializers.FileField(validators=[FileExtensionValidator(allowed_extensions=['csv'])])