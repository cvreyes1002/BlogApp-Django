from urllib import request

from django.shortcuts import render

from .models import user
from .forms import RegisterForm

# Create your views here.


def index(request):

    if request.method == "POST":
        form = RegisterForm(request.POST)
        # print(request.POST)
    
        if form.is_valid():
            username = form.cleaned_data["username"]
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            confirm_password = form.cleaned_data["confirm_password"]

            if password != confirm_password:
                form.add_error("confirm_password", "Passwords do not match")
                return render(request, "blog/index.html", {
                    "form": form
                })

            new_user = user(name=username, email=email, password=password)
            new_user.save()
    else:
        form = RegisterForm()
        return render(request, "blog/index.html", {
            "form": form
        })


def home_logged_in_no_results(request):
    return render(request, "blog/home-logged-in-no-results.html")
