from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout 
from django.http import HttpResponse
from .forms import RegisterForm

# Create your views here.

def loginpage(request):
    if request.method == "POST":
        usern = request.POST.get('usern')
        passw = request.POST.get('passw')
        user=authenticate(request,username=usern,password=passw)
        print(user)
        if user:
            login(request,user)#session
        else:
            print('no such user')
    return render(request,'login.html')

def logoutpage(request):
    logout(request)
    return HttpResponse('user logged out')


def registerpage(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(loginpage)
    else:
        form = RegisterForm()
    return redirect (request,'register.html',{'form':form})


