from django.db import models
from django.contrib.auth.models import User
from seller.models import *
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True , blank=True)
    name = models.CharField(max_length=150 , null=True)
    email = models.CharField(max_length=150,null=True)
    def __str__(self):
        return self.name
s

class Product(models.Model):
    pid = models.IntegerField(null=False, unique=True, primary_key=True)
    name = models.CharField(max_length=150, null=True)
    price = models.FloatField()
    image1 = models.ImageField(null=True, blank=True,upload_to='images/')
    image2 = models.ImageField(null=True, blank=True,upload_to='images/')
    image3 = models.ImageField(null=True, blank=True,upload_to='images/')
    image4 = models.ImageField(null=True, blank=True,upload_to='images/')
    digital = models.BooleanField(default=False, blank=False)
    brand = models.CharField(max_length=150, null=True)
    description = models.TextField(null=True,blank=True)
    technical_specs = models.TextField(null=True,blank=True)
    package_details = models.TextField(null=True,blank=True)
    note = models.CharField(max_length=10000, null=True)
    def __str__(self):
        return self.name

    @property
    def imageURL1(self):
        try:
            url = self.image1.url
        except:
            url = ''
        return url
    @property
    def imageURL2(self):
        try:
            url = self.image2.url
        except:
            url = ''
        return url
    @property
    def imageURL3(self):
        try:
            url = self.image3.url
        except:
            url = ''
        return url
    @property
    def imageURL4(self):
        try:
            url = self.image4.url
        except:
            url = ''
        return url
class Tag(models.Model):
    title = models.CharField(max_length=150)
    timestamp = models.DateTimeField(auto_now_add=True)
    product = models.ManyToManyField(Product,blank=True)
    def __str__(self):
        return self.title


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=False)
    transaction_id = models.CharField(max_length=150, null=True)

    def __str__(self):
        return str(self.id)

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        cart_total = 0.00
        for item in orderitems:
            cart_total += item.get_total
        return cart_total
    @property
    def get_cart_quantity(self):
        orderitems = self.orderitem_set.all()
        cart_quantity = 0
        for item in orderitems:
            cart_quantity += item.quantity
        return cart_quantity
    @property
    def shipping(self):
        shipping = False
        orderitems = self.orderitem_set.all()
        for item in orderitems:
            if item.product.digital == False:
                shipping = True
                break
        return shipping

class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True , null=True)
    order = models.ForeignKey(Order , on_delete=models.SET_NULL, blank=True , null=True)
    quantity = models.IntegerField(default=0,null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    @property
    def get_total(self):
        total = self.product.price* self.quantity
        return total

class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=150, null=False)
    city = models.CharField(max_length=150,null=False)
    state = models.CharField(max_length=150,null=False)
    zipcode = models.CharField(max_length=150,null=False)
    date_added= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address


