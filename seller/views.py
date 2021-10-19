from django.shortcuts import render,redirect
from seller.forms import *
from store.models import *
import store.views
from django.contrib.auth import authenticate, login , logout 
from django.contrib.auth.models import Group
# Create your views here.


def Register(request):
    if request.user.is_authenticated:
        print("registered")
        seller_group = Group.objects.get(name='Seller')
        if request.user in seller_group.user_set.all():
            return dashboard(request)
        else:
            return RegSeller(request)

    form = RegisterForm
    context = {"form"  : form}
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User.objects.create_user(username= username,
                                 email=email,
                                 password=password)
        user.save()
        login(request, user)
        customer = Customer(
            user=user,
            name=username,
            email= email
        )
        customer.save()
        return store.views.dashboard(request)
    context = {'form' : form}
    return render(request, 'seller/register_page.html' , context)

def loginUser(request):
    group = Group.objects.get(name='Seller')
    print("in login")
    if request.user.is_authenticated:
        print("authenticated")
        if request.user in group.user_set.all():
            return dashboard(request)
        else:
            return RegSeller(request)
    print("hello")
    if request.method == 'POST':
        print("hello")
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request ,username=email, password=password)
        if user is not None:
            login(request, user)
            print("sahi h")
            return RegSeller(request)
    else:
        print("get")
    return render(request , 'seller/login.html')

def RegSeller(request):
    form = sellerform
    print("in regesller")
    group = Group.objects.get(name='Seller')
    print(group.user_set.all() , request.user)
    if request.user in group.user_set.all():
        print("seller h bnhai apna")
        return dashboard(request)
    else:
        print("nhahi h ")
    context = {"form" : form}
    if request.method == 'POST':
        new__seller = Seller(
            user = request.user,
            name = request.user.username,
            email = request.POST.get('email'),
            phone = request.POST.get('phone'),
            office_address = request.POST.get('office_address'),
        )
        new__seller.save()
        seller_group = Group.objects.get(name='Seller')
        request.user.groups.add(seller_group)
        new_customer = Customer(
            user= request.user,
            name= request.user.username,
            email= new__seller.email,
        ) 
        new_customer.save()
        print("user added as seller")
    return render(request , 'seller/reg_seller.html', context)


def dashboard(request):
    #if not request.user.is_authenticated():
    #    return(Register(request))
    group = Group.objects.get(name='Seller')
    if not request.user in group.user_set.all():
        return RegSeller(request)
    print("in dash",request.user.username)    
    seller = Seller.objects.get(user= request.user)
    print(seller.general)
    analysis = seller.general
    context = {'username' : request.user.username, 'analysis' : analysis}
    return render(request, 'seller/dashboard.html',context)

def add_product(request):
    if request.method == 'POST':
        data = request.POST
        image = request.FILES.get('image')
        digi = False
        if data.get('digital') == 'True':
            digi = True
        else:
            digi = False
        new_product = Product(
            
            name = data.get('name'),
            price = data.get('price'),
            image1 = image,
            digital = digi,
            note = data.get('note').lower(),
        )
        new_product.save()
        all_tags = Tag.objects.all()
        for word in new_product.note.split(' '):
            if not all_tags.filter(title=word).exists():
                tag = Tag()
                tag.title = word
                tag.save()
                new_product.tag_set.add(tag)
            else:
                tag = all_tags.filter(title=word)
                new_product.tag_set.add(tag[0])

            

        new_si = Seller_Product(
            product = new_product,
            stock = data.get('quantity'),
            seller = Seller.objects.get(user=request.user)
        )
        new_si.save()
        return redirect('dashboard')

        
    return render(request,'seller/add_product.html')

def view_products(request):
    seller = Seller.objects.get(user=request.user)
    products = Seller_Product.objects.filter(seller=seller)
    context = {'products' : products}
    return render(request,'seller/view_products.html',context)

def logoutUser(request):
    logout(request)
    return loginUser(request)