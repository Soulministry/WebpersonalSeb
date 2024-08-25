from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return render(request, "deathcore/home.html")
def about(request):
    return render(request, "deathcore/about.html")

def contact(request):
    return render(request, "deathcore/contact.html")