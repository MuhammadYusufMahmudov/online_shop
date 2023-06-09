from django.contrib import admin
from .models import Product, Category


# Hammasini ozini adminidan registratsiya qilamiz

class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price', 'quantity']
    list_display_links = ['name']


admin.site.register(Product, ProductAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description']
    list_display_links = ['name']


admin.site.register(Category, CategoryAdmin)
# Register your models here.
