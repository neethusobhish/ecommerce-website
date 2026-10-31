from django.urls import path 
from .views import *

urlpatterns = [

    path('login',loginpage, name='login'),
    path('logout',logoutpage,name='logout'),
    path('register',registerpage,name='register')

]