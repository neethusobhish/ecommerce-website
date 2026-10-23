from django.shortcuts import render
from .models import Products

# Create your views here.


def allproductspage(request):
    pro= Products.objects.all()
    return render(request,'allproducts.html',{'pro':pro})

def productdetailpage(request,pid):
    pro= Products.objects.get(id=pid)
    return render(request,'prodetails.html',{'pro':pro})