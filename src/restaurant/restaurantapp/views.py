from django.shortcuts import render
# from django.templates import loader
from django.http import HttpResponse, HttpResponseRedirect
from .models import restaurants_list, Cuisines, Menu
# Create your views here.

def home_view(request):
    return render(request, "home.html", {})

def restaurant_list_view(request):
    queryset = restaurants_list.objects.all()
    context = {
        "obj" : queryset
    }
    return render(request, "restaurant/restaurant_list.html", context)

def restaurant_view(request,id):
    queryset= restaurants_list.objects.all(id=id)
    queryset2= queryset.cuisines.all()
    context = {
        'obj2' : queryset,
        'obj' : queryset2
    }
    return render(request, "restaurant/restaurant_view.html",context)

def add(request):
    return render(request, "restaurant/add.html",{})

def addrecord(request):
    x = request.POST['add name']
    y = request.POST['Your Description']
    z = request.POST['Add Location']
    a = request.POST['SI', 'IT', 'PU', 'CH']
    b = request.POST['Y']
    c = request.POST['Your contact no.']
    d = request.POST['Your Email']
    restaurant= restaurants_list(Reataurant_name=x, Description=y, Location=z, Cuisines=a, veg=b, Contect_no=c, Email=d )
    restaurant.save()
    return HttpResponseRedirect(reverse(restaurant_list))

    

