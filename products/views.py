from django.shortcuts import render,redirect
from .models import *
from .forms import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializer import *

# Create your views here.


def allproductspage(request):
    pro= Products.objects.all()
    return render(request,'allproducts.html',{'pro':pro})

def productdetailpage(request,pid):
    pro= Products.objects.get(id=pid)
    return render(request,'prodetails.html',{'pro':pro})

def allcategorypage(request):
    cat = Category.objects.all()
    return render (request,'allcategory.html',{'cat':cat})


def categoryitemspage(request,cid):
    catitems = Products.objects.filter(cat_id=cid)
    return render(request,'categoryitems.html',{'catitems':catitems})


def addproductpage(request):
    if request.method == 'POST':
        form = ProductForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect(allproductspage)
    else:
        form = ProductForm() 
    return render(request,'addproducts.html',{'form':form}) 


def addcategorypage(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(allcategorypage)
    else:
        form = CategoryForm()
    return render(request,'addcategory.html',{'form':form})

def editproductpage(request,pid):
    pro = Products.objects.get(id=pid)

    if request.method == 'POST':
        form = ProductForm(request.POST,request.FILES,instance=pro)
        if form.is_valid():
            form.save()
            return redirect(allproductspage)
    else:
        form = ProductForm(instance=pro)
    return render(request,'editproduct.html',{'form':form})

def deleteproductpage(request,pid):
    pro = Products.objects.get(id=pid)

    if request.method=='POST':
        pro.delete()
        return redirect(allproductspage)
    else:
        return render(request,'deleteproduct.html',{'pro':pro})
    # pro.delete()
    # return redirect(allproductspage)


# api

@api_view(['GET'])
def allproductsapi(request):
    product= Products.objects.all()
    serializer = ProductSerializer(product,many=True)
    return Response(serializer.data)


@api_view(['GET'])
def allcategoryapi(request):
    category = Category.objects.all()
    serializer = CategorySerializer(category,many=True)
    return Response(serializer.data)
    