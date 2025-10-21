from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import F
from .models import InventoryItem
from .forms import InventoryItemForm


# Helper function to get low stock count
def get_low_stock_count():
    return InventoryItem.objects.filter(quantity__lt=F('reorder_level')).count()


def staff_inventory(request):
    items = InventoryItem.objects.all()
    context = {
        'inventory_items': items,
        'low_stock_count': get_low_stock_count(),  # Add low_stock_count to context
    }
    return render(request, 'staff_inventory.html', context)


def update_inventory(request, item_id):
    item = get_object_or_404(InventoryItem, id=item_id)
    if request.method == 'POST':
        form = InventoryItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('staff_inventory')
    else:
        form = InventoryItemForm(instance=item)

    context = {
        'form': form,
        'item': item,
        'low_stock_count': get_low_stock_count(),  # Add low_stock_count here too
    }
    return render(request, 'update_inventory.html', context)
