from .models import InventoryItem
from django.db.models import F
from .models import InventoryItem
from django.db.models import F

def low_stock_notification(request):
    low_stock_items = InventoryItem.objects.filter(quantity__lt=F('reorder_level'))
    return {
        'low_stock_count': low_stock_items.count(),
        'low_stock_items': low_stock_items
    }
