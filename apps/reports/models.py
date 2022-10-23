from django.db import models
# Create your models here.
class Customer(models.Model):
    
    firstname = models.CharField(max_length=255, null=False)
    lastname = models.CharField(max_length=255, null=False)
    
    def __str__(self):
        return f'{self.firstname} {self.lastname}'
    
    def __repr__(self):
        return f'{self.firstname} {self.lastname}'
    
    
class Product(models.Model):
    
    name = models.CharField(max_length=512, null=False)
    cost = models.DecimalField(max_digits=20, decimal_places=10, null=False)
    
    def __str__(self):
        return f'{self.name}'
    
    def __repr__(self):
        return f'{self.name}'
    
    
class Order(models.Model):
    
    customer = models.ForeignKey(Customer, null=False, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, db_table="order_products")
    
    def __str__(self):
        return f'{self.customer} -> {self.products}'
    
    def __repr__(self):
        return f'{self.customer} -> {self.products}'
