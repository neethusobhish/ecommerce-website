from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout 
from django.http import HttpResponse

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


