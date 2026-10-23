from django.urls import path
from .views import *



urlpatterns = [

    path('all_products',allproductspage),
    path('prodetails/<int:pid>',productdetailpage,name='prodetails')
]