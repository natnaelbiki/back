from django.contrib import admin
from .models import Product, Cart, CartItem

admin.site.register(Product)
admin.site.register(CartItem)
admin.site.register(Cart)


# Register your models here.
