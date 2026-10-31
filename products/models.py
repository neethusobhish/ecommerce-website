from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
        name = models.CharField(max_length=100)
        des = models.TextField()

        def __str__(self):
            return self.name


class Products(models.Model):

    name = models.CharField(max_length=20)
    description = models.TextField()
    price = models.IntegerField()
    image = models.ImageField(null=True,upload_to='photos')
    stock = models.PositiveIntegerField()
    created_at = models.DateTimeField(null=True,auto_now_add=True)
    updated_at = models.DateTimeField(null=True,auto_now=True)
    is_available = models.BooleanField()
    slug = models.SlugField(null=True,blank=True)
    cat = models.ForeignKey(Category,on_delete=models.CASCADE,null=True)


    def save(self):
        self.slug = slugify(self.name)
        super().save()

    def __str__(self):
        return self.name

class Customer(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    phone = models.BigIntegerField()
    address = models.TextField()
    city = models.CharField()
    pincode = models.CharField()

    def __str__(self):
        return self.user.username  

class Cart(models.Model):
    user = models.ForeignKey(Customer,on_delete=models.CASCADE,null=True)
    created_at = models.DateTimeField(null=True,auto_now_add=True)

    def __str__(self):
        return self.user.user.username

class CartItem(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null = True)
    # cart = models.ForeignKey(Cart,on_delete=models.CASCADE,null=True,blank=True)
    product = models.ForeignKey(Products,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def total_price(self):
        return self.product.price*self.quantity



    def __str__(self):
        return self.user.first_name


class Order(models.Model):

    status = [
        ('Pending','PENDING'),
        ('Shipped','SHIPPED'),
        ('Deliverd','DELIVERD'),
        ('Cancelled','CANCELLED')
    ]

    pending_status = [
        ('Pending','PENDING'),
        ('Paid','PAID'),
        ('Failed','FAILED')
    ]

    user = models.ForeignKey(Customer,on_delete=models.CASCADE)
    total_amount = models.DecimalField()
    order_date = models.DateField()
    status = models.CharField(choices=status)
    payment_method = models.CharField()
    payment_status= models.CharField(choices=pending_status)

    def __str__(self):
        return self.user.user.username

   