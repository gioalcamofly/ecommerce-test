from django.db import models
# Create your models here.
class Customer(models.Model):
    
    firstname = models.CharField(max_length=255, null=False)
    lastname = models.CharField(max_length=255, null=False)
    
    def __str__(self) -> str:
        return f'{self.firstname} {self.lastname}'
        
    
class OrderProduct(models.Model):
    
    product = models.ForeignKey("Product", null=False, on_delete=models.CASCADE)
    order = models.ForeignKey("Order", null=False, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    quantity = models.IntegerField(null=False, default=1)
     
    def __str__(self) -> str:
            return f'{self.order} -> {self.product}'
        
class Product(models.Model):
    
    name = models.CharField(max_length=512, null=False)
    cost = models.DecimalField(max_digits=20, decimal_places=10, null=False)
    
    def __str__(self) -> str:
        return f'{self.name}'
        
class Order(models.Model):
    
    customer = models.ForeignKey(Customer, null=False, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through='OrderProduct')
    
    def __str__(self) -> str:
        return f'{self.customer} -> {self.products}'

        