from django.urls import path
from .views import restaurant_list_view, restaurant_view, add, addrecord

app_name = 'restaurants'
urlpatterns =[
    path('',restaurant_list_view , name='list'),
    path('restaurant/<int:id>',restaurant_view , name='view'),
    path('restaurant/add/', add, name='add'),
    path('restaurant/add/addrecord', addrecord, name='addrecord'),

    


]