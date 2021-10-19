from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings 

urlpatterns = [
    path('',views.Register, name = 'register'),
    path('login/',views.loginUser, name = 'login'),
    path('regseller/',views.RegSeller , name = "RegSeller"),
    path('dashboard' , views.dashboard,name = "dashboard"),
    path('add_product' , views.add_product, name="add_product"),
    path('view_products',views.view_products,name="view_products"),
    path('logout',views.logoutUser,name='logout')

]

urlpatterns += static(settings.MEDIA_URL, 
                              document_root=settings.MEDIA_ROOT) 