from django.contrib import admin
from .models import Category, Product, ContactMessage, CartItem

admin.site.register(Category)
admin.site.register(Product)
# إظهار الرسائل والسلة للإدارة
admin.site.register(ContactMessage)
admin.site.register(CartItem)