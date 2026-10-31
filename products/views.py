from django.shortcuts import render,redirect,get_object_or_404
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


# add product to cart (with choosen quantity)
def add_to_cart(request,product_id):
    if not request.user.is_authenticated:
        return redirect('login')

    if request.method =='POST':
        prodct = Products.objects.get(id=product_id)
        quantity = int(request.POST.get('quantity',1))

    item = CartItem.objects.filter(user=request.user, product=prodct).first()
    if item:
        item.quantity +=quantity
        item.save()
    else:
        CartItem.objects.create(user=request.user,product=prodct,quantity=quantity)

    return redirect(allproductspage)


# 4. View cart: all items + grand total
def view_cartpage(request):
    if not request.user.is_authenticated:
        return redirect("login")

    items = CartItem.objects.filter(user=request.user)
    grand_total = 0
    for item in items:
        grand_total += item.total_price()

    return render(request, "cart.html", {"items": items, "grand_total": grand_total})


# 5. Increase quantity by 1
def increase_quantity(request, item_id):
    if not request.user.is_authenticated:
        return redirect("login")

    item =CartItem.objects.get(id=item_id, user=request.user)
    item.quantity += 1
    item.save()
    return redirect(view_cartpage)


# 6. Decrease quantity by 1 (remove the item if it reaches 0)
def decrease_quantity(request, item_id):
    if not request.user.is_authenticated:
        return redirect("login")

    item = CartItem.objects.get(id=item_id, user=request.user)
    item.quantity -= 1
    if item.quantity <= 0:
        item.delete()
    else:
        item.save()
    return redirect(view_cartpage)


# 7. Remove an item completely
def remove_item(request, item_id):
    if not request.user.is_authenticated:
        return redirect("login")

    item =CartItem.objects.get( id=item_id, user=request.user)
    item.delete()
    return redirect(view_cartpage)












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
    