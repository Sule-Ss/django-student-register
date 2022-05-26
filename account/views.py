from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
# Create your views here.

def home(request):
    return render(request, "home.html")

def login_request(request):
    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username= username, password = password)

        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            return render(request, "account/login.html", messages.error(request, "username or password is undefine!"))

    return render(request, "account/login.html")

def signup_request(request):
    if request.user.is_authenticated:
        return redirect("home")
        
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        firstname = request.POST["firstname"]
        lastname = request.POST["lastname"]
        password = request.POST["password"]
        repassword = request.POST["repassword"]

        if password == repassword:
            if User.objects.filter(username=username).exists():
                return render(request, "account/signup.html", messages.error(request, "Username already exists. Please choose another!"))
            else:
                if User.objects.filter(email=email).exists():
                    return render(request, "account/signup.html", messages.error(request, "Username already exists. Please choose another!"))
                else:
                    user = User.objects.create_user(username=username, email=email, first_name=firstname, last_name=lastname, password=password)
                    user.save()
                    return redirect("login")
        else:
            return render(request, "account/signup.html", messages.error(request, "Passwords does not match!"))
    return render(request, "account/signup.html")

def logout_request(request):
    logout(request)
    return redirect("home")
