from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings

# Create your views here.
def home(request):
    return render(request,"home.html")

def home_view(request):
    return HttpResponse(f"<h1>welcome to{settings.RESTAURANT_NAME}</h1>")
