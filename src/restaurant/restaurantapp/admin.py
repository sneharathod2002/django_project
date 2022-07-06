from django.contrib import admin

# Register your models here.
from .models import Cuisines, restaurants_list, Menu

admin.site.register(Menu)
admin.site.register(Cuisines)
admin.site.register(restaurants_list)

