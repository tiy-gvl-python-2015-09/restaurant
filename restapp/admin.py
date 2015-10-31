from django.contrib import admin

# Register your models here.
from restapp.models import Profile, Order, Item, ItemCounter

admin.site.register(Profile)
admin.site.register(Order)
admin.site.register(Item)
admin.site.register(ItemCounter)