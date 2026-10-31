from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static






urlpatterns = [

    path('all_products',allproductspage,name='allproduct'),
    path('prodetails/<int:pid>',productdetailpage,name='prodetails'),
    path('allcategory',allcategorypage),
    path('categoryitems/<int:cid>',categoryitemspage,name='categoryitems'),
    path('addproducts',addproductpage,name='addproduct'),
    path('addcategory',addcategorypage),
    path('editproduct/<int:pid>',editproductpage,name='edit_products'),
    path('deletepro/<int:pid>',deleteproductpage,name='delete_product'),
    path('allproductapi',allproductsapi),
    path('allcategoryapi',allcategoryapi),
    path('cart',view_cartpage,name='viewcart'),
    path("cart/increase/<int:item_id>/", increase_quantity, name="increase_quantity"),
    path("cart/decrease/<int:item_id>/", decrease_quantity, name="decrease_quantity"),
    path("cart/remove/<int:item_id>/", remove_item, name="remove_item"),
    
    
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)