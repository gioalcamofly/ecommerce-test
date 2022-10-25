from django.db import models
# Create your models here.
class Customer(models.Model):
    
    firstname = models.CharField(max_length=255, null=False)
    lastname = models.CharField(max_length=255, null=False)
    
    def __str__(self):
        return f'{self.firstname} {self.lastname}'
        
    
class Product(models.Model):
    
    name = models.CharField(max_length=512, null=False)
    cost = models.DecimalField(max_digits=20, decimal_places=10, null=False)
    
    def __str__(self):
        return f'{self.name}'
    
        
class Order(models.Model):
    
    customer = models.ForeignKey(Customer, null=False, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through='OrderProduct')
    
    @property
    def order_price(self):
        return sum(order_product.total_price for order_product in self.products)
    
    def __str__(self):
        return f'{self.customer} -> {self.products}'
    
class OrderProduct(models.Model):
    
    product = models.ForeignKey(Product, null=False, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, null=False, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    quantity = models.IntegerField(null=False, default=1)
    
    @property
    def total_price(self):
        return self.product.cost * self.quantity
    
    def __str__(self):
            return f'{self.order} -> {self.product}'

        