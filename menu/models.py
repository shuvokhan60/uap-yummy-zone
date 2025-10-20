from django.db import models
from django.contrib.auth.models import User
from decimal import Decimal, InvalidOperation


class FoodItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    # ✅ Default price added, so even if blank/null, Django won’t crash
    price = models.DecimalField(max_digits=20, decimal_places=2, default=Decimal('0.00'))
    image = models.ImageField(upload_to='menu_images/', blank=True, null=True)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    food_item = models.ForeignKey(FoodItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    # ✅ Default added here too for safety
    total_price = models.DecimalField(max_digits=20, decimal_places=2, default=Decimal('0.00'))
    is_paid = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.food_item.name}"
