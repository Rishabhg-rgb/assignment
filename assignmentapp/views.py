from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout,login as auth_login

# Create your views here.


def dashboard(request):
    if request.user.is_authenticated:
        return render(request,'dashboard.html')
    else:
        return redirect('/createuser')

def createuser(request):
    if request.method=="POST":
        fname = request.POST['fname']
        lname = request.POST['fname']
        Username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirmpassword = request.POST['confirmpassword']
        address = request.POST['address']
        usertype = request.POST['usertype'].value

        if confirmpassword == password:
            user = User.objects.create_user(Username,email,password)
            user.first_name = fname+" "+lname+" "+ usertype
            user.last_name = address
            user.save()
            return redirect('/dashboard')
    else:
        return render(request,"signup.html")


def login(request):
    if request.method=="POST":
        Username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=Username,password=password)
        if user is not None:
            auth_login(request,user)
            return redirect('/dashboard')
        else:
            return HttpResponse("Wrong credentials")
    else:
        return render(request,'login.html')
    

def handlelogout(request):
    logout(request)
    return redirect('/login')
    