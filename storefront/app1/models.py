from django.db import models 
from django.contrib.auth.models import User

# Create your models here.
class customer(models.Model):
    cst = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    customer_id = models.AutoField.primary_key= True
    customer_name = models.CharField(max_length=50)
    customer_email = models.CharField(max_length=100)

    def __str__(self):
        return self.customer_name 

class product(models.Model):
    product_id = models.AutoField.primary_key=True
    product_name = models.CharField(max_length=20)
    product_desc = models.CharField(max_length=255) 
    image = models.ImageField(null=True,blank=True)
    slug = models.SlugField(unique=True, null=True, blank=True)
    price = models.FloatField()

class order(models.Model):
    customer = models.ForeignKey(customer, on_delete= models.SET_NULL, blank=True,null=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False,)
    transaction_id = models.CharField(max_length=100, null=True) 
    
    def __str__(self):
        return str(self.transaction_id)
class orderItem(models.Model):
    product = models.ForeignKey(product, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(order, on_delete=models.SET_NULL,null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

class shipping(models.Model):
    customer = models.ForeignKey(customer, on_delete=models.SET_NULL,null=True)
    address = models.TextField(blank=True , max_length=300)
    city = models.CharField(max_length=64 )
    state = models.CharField (max_length=64)
    zipcode = models.CharField(max_length=8)
    timestamp = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.address
    
"""class cart(models.Model):
    cart_id = models.AutoField.primary_key=True
    product_id 	= models.ForeignKey('product', on_delete=models.CASCADE)
    customer_id = models.ForeignKey('customer', on_delete=models.CASCADE) 
    total_amount = models.CharField(max_length=50)
    timestamp = models.DateTimeField()

class payment(models.Model):
    paymnet_id = models.AutoField.primary_key=True
    payment_mode = models.CharField(max_length=50)
    total_amount = models.CharField(max_length=50) 
    timestamp = models.DateTimeField() 
class newarrival(models.Model):
    product_id 	= models.ForeignKey('product', on_delete=models.CASCADE) 
    product_desc = models.CharField(max_length=255)
    price = models.FloatField()"""