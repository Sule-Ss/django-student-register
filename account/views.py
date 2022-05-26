from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from django.contrib import messages
# Create your views here.

def home(request):
    return render(request, "home.html")

def login_request(request):
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
    return render(request, "account/signup.html")

def logout_request(request):
    return redirect("/")
