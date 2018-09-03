from orders.models import Order
from orders.models import OrderItem
from django.contrib import admin

# Register your models here.
admin.site.register(Order)
admin.site.register(OrderItem)
