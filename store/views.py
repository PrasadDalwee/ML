from django.shortcuts import render , redirect
from .models import *
from seller.models import *
from django.http import JsonResponse
import json
import datetime
from django.contrib.auth import authenticate, login , logout 
from .filters import OrderFilter
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Q
from django.http import QueryDict
import copy
from django.views.decorators.csrf import csrf_exempt



######## ML imports

import pandas as pd
import os
import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel





# Create your views here.
addProducts = True

def add_products():
    if not addProducts:
        return
    products = Product.objects.all()
    products.delete()
    return
    df=pd.read_csv("store/amazon.csv")
    mean_value = 105.556
    df['price'].fillna(value=mean_value, inplace = True)
    for i, p in df.iterrows():
        name = p['product_name']
        price = p['price']
        
        if type(price) == type(1.9889):
            pass
        else:
            price = p['price'][1:]
            try:
                price = float(price)
            except ValueError:
                price = 105.55
        if not price:
            continue
        if price == 0:
            price= 10.556
        print(price)
        brand = p['manufacturer']
        description = p['description']
        technical_specs = p['product_information']
        new_product = Product(
        
        name = name,
        price = price,
        digital = False,
        brand = brand,
        description = description,
        technical_specs = technical_specs,

        )
        new_product.save()
    print("success!!!")

        



def dashboard(request):
    if request.method == 'POST':
        return store(request)
    addProducts = False
    df=pd.read_csv("store/amazon.csv")

    products = df.iloc[:100]
    dash_products = products
    latest_prod = products
    latest_prod = latest_prod[::-1]

    if request.user.is_authenticated:
        customer = request.user.customer
        order,created = Order.objects.get_or_create(customer=customer)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_quantity
    else:
        items = []
        order = {'get_cart_total' : 0 , 'get_cart_quantity'  : 0 ,'shipping' : False}
        cartItems = order['get_cart_quantity']

    context = {
     'products' : products ,
     'dash_products' : dash_products, 
     'cartItems' : cartItems ,
     'latest_prod' : latest_prod}
    return render(request, 'store/dashboard.html', context)

def store(request):


    if request.user.is_authenticated:
        customer = request.user.customer
        order,created = Order.objects.get_or_create(customer=customer)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_quantity
    else:
        items = []
        order = {'get_cart_total' : 0 , 'get_cart_quantity'  : 0 ,'shipping' : False}
        cartItems = order['get_cart_quantity']
    Allproducts = Product.objects.all()
    context = {'products' : Allproducts , 'cartItems' : cartItems}
    return render(request,'store/store.html', context)
    
    # if request.method == 'POST':
    #     query = request.POST
    #     note = query.get('tag')   
    #     if note is None: 
    #         Allproducts = Allproducts.distinct
    #         context = {'products' : Allproducts , 'cartItems' : cartItems}
    #         return render(request,'store/store.html', context)
    #     note = note.lower().split()
    #     product_set = Product.objects.none()
    #     for word in note:
    #         print(word)
    #         print(len(Allproducts))
    #         lookups = Q(tag__title__icontains = word)
    #         product_set = (product_set | Allproducts.filter(lookups))
    #     product_set = product_set.distinct()
    #     print(len(product_set), "is the totals")
    #     # counting sort
    #     rank_list = [[]]*(len(note)+1)
    #     for product in product_set.all():
    #         score = 0 
    #         print(product.tag_set.all())
    #         for word in note:
    #             print(word)
    #             if product.tag_set.filter(title = word).exists():
    #                 score += 1
    #         print(product , score)
    #         rank_list[len(note) - score].append(product)
    #         print("appending " , product ,"in " , len(note) - score)
    #     #rank_list.reverse()
    #     #Allproducts = [product for rank in rank_list for product in rank]
    #     prod_list = []
    #     for pl in rank_list:
    #         print(len(pl))
    #         for p in pl:
    #             prod_list.append(p)
    #     prod_list.reverse()
    #     prod_list = list(set(prod_list))
    #     Allproducts = prod_list
    #     print(Allproducts , "\nfinal order")


        

    # context = {'products' : Allproducts , 'cartItems' : cartItems}
    # return render(request,'store/store.html', context)
    

def login_user(request):
    if request.user.is_authenticated:
        return dashboard(request)
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request ,username=username, password=password)
        if user is not None:
            request.method = 'GET'
            login(request, user)
            return  dashboard(request)
    return render(request , 'store/login.html')

def logout_user(request):
    logout(request)
    return dashboard(request)

    return render(request,'store/login.html')
def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order,created = Order.objects.get_or_create(customer=customer)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_quantity
    else:
        items = []
        order = {'get_cart_total' : 0 , 'get_cart_quantity'  : 0}
        cartItems = order['get_cart_quantity']
    context = {'items' : items ,'order' : order , 'cartItems' : cartItems ,'shipping' : False}
    return render(request,'store/cart.html', context)

def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order,created = Order.objects.get_or_create(customer=customer)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_quantity
    else:
        items = []
        order = {'get_cart_total' : 0 , 'get_cart_quantity'  : 0}
        cartItems = order['get_cart_quantity']
    context = {'items' : items ,'order' : order, 'cartItems' : cartItems ,'shipping' : False}
    return render(request,'store/checkout.html', context)

@csrf_exempt
def updateItem(request):
    productid = request.POST.get('id')
    action = request.POST.get('action')
    customer = request.user.customer
    product = Product.objects.get(id=productid)
    order,created = Order.objects.get_or_create(customer=customer)
    orderItem,created = OrderItem.objects.get_or_create(order=order , product=product) 
    if action == 'add':
        orderItem.quantity += 1
        sp = Seller_Product.objects.all().filter(product=product)
        cart_n = sp[0].cart_no
        sp.update(cart_no = cart_n+1)
    elif action == 'remove':
        orderItem.quantity -= 1
        sp = Seller_Product.objects.all().filter(product=product)
        cart_n = sp[0].cart_no
        sp.update(cart_no = cart_n-1)

    sp[0].save()
    orderItem.save()
    if orderItem.quantity <= 0:
        orderItem.delete()
    context = {'cart_quantity' : order.get_cart_quantity , 'cart_total' : order.get_cart_total , 'item_quantity' : orderItem.quantity , 'item_total' : orderItem.get_total}
    return JsonResponse(context, safe=False)

def ProcessOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)
    if request.user.is_authenticated:
        customer = request.user.customer
        order,created = Order.objects.get_or_create(customer=customer)
        total = float(data['form']['total'])
        order.transaction_id = transaction_id

        if total == order.get_cart_total:
            order.complete = True
        order.save()
        for item in order.orderitem_set.all():
            product = Seller_Product.objects.all().filter(product= item.product)
            initial_sale = product[0].sale
            product.update(sale = initial_sale+item.quantity)


        if order.shipping == True:
            ShippingAddress.objects.create(
                customer=customer,
                order=order,
                address=data['shipping']['address'],
                city = data['shipping']['city'],
                state = data['shipping']['state'],
                zipcode = data['shipping']['zipcode'],
            )
    else:
        print('user is not logged in..')
    return JsonResponse('payment complete', safe=False)

def product_detail(request ,id):
    product = Product.objects.get(id=id)
    all_prod = Product.objects.all()
    other_prod = []
    for p in all_prod:
        if str(p.id) != str(id):
            other_prod.append(p)
    print(other_prod[0], "this is the firs tprpduct")
    context = {'product' : product, 'other_products' : other_prod[:3]}
    # sp = Seller_Product.objects.all().filter(product=product)
    # visit = sp[0].visits
    # sp.update(visits = visit+1)
    #sp.save()

    return render(request, 'store/single.html', context)