from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from .models import Restaurant

# Create your views here.

def home(request):
    return render(request,"home.html")
    
def home_view(request):
    restaurant = Restaurant.objects.first()
    if restaurant:
        return HttpResponse(f"<h1>welcome to{restaurant.name}</h1>")
    else:
        return HttpResponse("<h1>welcome to our Restaurant</h1>")

