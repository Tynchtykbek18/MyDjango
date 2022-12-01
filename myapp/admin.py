from django.contrib import admin
from .models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'order_name']
    list_display_links = list_display
    search_fields = ['order_name']
