from django.urls import path
from . import views
from .views import *

urlpatterns = [
   
    path('' , views.index , name='index'),
    path('login',views.login_view , name='login'),
    path('register', views.register_view , name='register'),
    path('employee' , views.employee , name='employee'),
    path('admin_panel' , views.admin , name='admin_panel'),
    path('addbonus' , views.addbonus , name='addbonus'),

    
] 
