from django.db import models
from django.contrib.auth.models import User
from store.models import *

class Seller(models.Model):
    user = models.OneToOneField(User , null=True ,on_delete = models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=12, null=True)
    date_created = models.DateTimeField(auto_now_add=True ,  null=True)
    office_address = models.CharField(max_length=200, null=True)
    USERNAME_FIELD = 'email'
    def __str__(self):
        return self.name

    
    @property
    def general(self):
        sp = Seller_Product.objects.all().filter(seller=self)
        no_of_sale = 0
        no_of_visits = 0 
        carts = 0
        total_revenue = 0.00
        for s in sp:
            no_of_sale += s.sale
            no_of_visits += s.visits
            carts += s.cart_no
            total_revenue += s.product.price*s.sale
        return {'no_of_sale' : no_of_sale , 'no_of_visits' : no_of_visits , 'carts' : carts , 'total_revenue' : total_revenue , 'view_to_sale' : round((no_of_sale/(no_of_visits+1))*100,2),  }



class Seller_Product(models.Model):
    product = models.ForeignKey('store.Product', on_delete=models.CASCADE)
    stock = models.IntegerField()
    seller = models.ForeignKey('Seller' , on_delete=models.CASCADE)
    visits = models.IntegerField(default=0)
    sale = models.IntegerField(default=0)
    cart_no = models.IntegerField(default=0)