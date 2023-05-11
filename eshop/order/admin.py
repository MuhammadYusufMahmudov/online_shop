from django.contrib import admin
from .models import Order, OrderDetail

# Hammasini ozini adminidan registratsiya qilamiz

admin.site.register(Order)
admin.site.register(OrderDetail)

# Register your models here.
