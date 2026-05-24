from urllib import request

from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render

# from .models import User (Not needed since we are using a ModelForm)
from .forms import RegisterForm

# Create your views here.


def index(request):

    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            # username = form.cleaned_data["username"]
            # email = form.cleaned_data["email"]
            # password = form.cleaned_data["password"]
            # confirm_password = form.cleaned_data["confirm_password"]

            # if password != confirm_password:
            #     form.add_error("confirm_password", "Passwords do not match")
            #     return render(request, "blog/index.html", {
            #         "form": form
            #     })

            # new_user = User(name=username, email=email, password=password)
            # new_user.save()
            form.save()
            return HttpResponseRedirect("/register")
        else:
            return render(request, "blog/index.html", {
                "form": form
            })
    else:
        form = RegisterForm()
        return render(request, "blog/index.html", {
            "form": form
        })


def register(request):
    return HttpResponse("Register page")
