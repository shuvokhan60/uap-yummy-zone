from django.contrib import admin
from .models import FoodItem, Order

@admin.register(FoodItem)
class FoodItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'available')
    search_fields = ('name',)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'food_item', 'quantity', 'total_price', 'is_paid', 'created_at')
    list_filter = ('is_paid',)
