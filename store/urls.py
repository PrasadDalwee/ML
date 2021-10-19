from django.urls import path,include
from . import views
from seller.views import *

urlpatterns = [
    path('store', views.store, name='store'),
    path('' , views.dashboard, name='dashboard_customer'),
    path('cart/', views.cart, name='cart'),
    path('login/', views.login_user, name='login_user'),
    path('logout/', views.logout_user, name='logout_user'),

    path('checkout/', views.checkout, name='checkout'),
    path('update_item/' ,views.updateItem,name="update_item"),
    path('ProcessOrder/' , views.ProcessOrder,name="ProcessOrder"),
    path('product/<str:id>', views.product_detail,name="product_detail"),
    #path('filter/<str:query>' , views.filter_store, name = "filterby"), under development
]

