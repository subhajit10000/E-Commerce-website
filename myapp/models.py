from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    mobile=models.CharField(max_length=15, verbose_name="Contact number")


class Category(models.Model):
    cat_name=models.CharField(max_length=100, verbose_name="Category Name")
    desc=models.CharField(max_length=255, verbose_name="Descriptions")
    def __str__(self):
        return self.cat_name

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/')
    brand=models.CharField(max_length=50)
    waranty=models.CharField(max_length=255)
    inbox=models.CharField(max_length=255)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(self):
        return self.name   

class CartItem(models.Model):
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	quantity = models.PositiveIntegerField(default=0)
	user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
	date_added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f'{self.quantity} x {self.product.name}'  


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    date_ordered = models.DateTimeField(auto_now_add=True)
    payment_status=models.CharField(max_length=255)
    payment_id=models.CharField(max_length=255)
    address=models.TextField()     




