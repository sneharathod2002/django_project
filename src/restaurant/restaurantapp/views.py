from django.shortcuts import render
# from django.templates import loader
from django.http import HttpResponse 
from .models import restaurants_list, Cuisines, Menu
# Create your views here.

def home_view(request):
    return render(request, "home.html", {})

def restaurant_list_view(request):
    queryset = restaurants_list.objects.all()
    context = {
        "obj" : queryset
    }
    return render(request, "restaurantapp/restaurant_list.html", context)
