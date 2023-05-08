from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product_image=models.ImageField(upload_to = 'Media')
    dicount_price = models.PositiveIntegerField()
    
    def __str__(self):
        return str(self.user)

class Cart(models.Model):
    usercart = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    
    @property
    def total_cost(self):
        return self.quantity*self.product.dicount_price
    
    
    def __str__(self):
        return str(self.usercart)   
