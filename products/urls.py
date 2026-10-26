from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static






urlpatterns = [

    path('all_products',allproductspage),
    path('prodetails/<int:pid>',productdetailpage,name='prodetails'),
    path('allcategory',allcategorypage),
    path('categoryitems/<int:cid>',categoryitemspage,name='categoryitems'),
    path('addproducts',addproductpage),
    path('addcategory',addcategorypage),
    path('editproduct/<int:pid>',editproductpage,name='edit_products'),
    path('deletepro/<int:pid>',deleteproductpage,name='delete_product')
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)