from django.shortcuts import render

# Create your views here.
def index(request):
    if request.method == "POST":
        # print(request.POST)
        return render(request, "blog/home-logged-in-no-results.html")

    return render(request, "blog/index.html")


def home_logged_in_no_results(request):
    return render(request, "blog/home-logged-in-no-results.html")