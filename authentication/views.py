from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from trees.models import *

def home(request):
    return render(request, "authentication/index.html")

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            firstname = user.first_name
            lastname = user.last_name
            zote = Miti.objects.get(pk=10) # fun is trying all madness there is
            price = zote.price
            gapi = zote.quantity
            #return render(request, "authentication/index.html", {'firstname':firstname,'lastname':lastname})
            return render(request,"authentication/index.html",{'name':zote, 'price':price, 'gapi':gapi})
        
        else:
            messages.error(request, "Invalid Credentials")
            return redirect('home')

    return render(request, "authentication/signin.html")

def signup(request):

    if request.method == "POST":
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        confirmpwd = request.POST['confirmpwd']

        if User.objects.filter(username=username):
            messages.error(request, "username is taken")
            return redirect('home')
        
        if User.objects.filter(email=email):
            messages.error(request, "email already registered")
            return redirect('home')
        
        if len(username) > 12:
            messages.error(request, "username too long")

        if password != confirmpwd:
            messages.error(request, "passwords should match")



        myuser = User.objects.create_user(username,email,password)
        myuser.first_name = firstname
        myuser.last_name = lastname

        myuser.save()
        messages.success(request, "account created successifuly")

        return redirect('signin')



    return render(request, "authentication/signup.html")

def signout(request):
    logout(request)
    messages.success(request, "Logged out ")
    return redirect('home')