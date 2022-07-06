from django.urls import path
from .views import restaurant_list_view

app_name = 'restaurants'
urlpatterns =[
    path('',restaurant_list_view , name='list'),



]