from django.contrib import admin
from .models import Customer, Seller, Product, Sale

# Register your models here.
admin.site.register(Customer)
admin.site.register(Seller)
admin.site.register(Product)
admin.site.register(Sale)
