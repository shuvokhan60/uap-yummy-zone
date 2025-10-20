from django.shortcuts import render, redirect, get_object_or_404
from .models import InventoryItem

def staff_home(request):
    context = {
        'staff_name': request.user.first_name or request.user.username
    }
    return render(request, 'staff.html', context)


def staff_inventory(request):
    inventory_items = InventoryItem.objects.all()
    return render(request, 'staff_inventory.html', {'inventory_items': inventory_items})

def update_inventory(request, item_id):
    item = get_object_or_404(InventoryItem, id=item_id)

    if request.method == 'POST':
        new_quantity = request.POST.get('quantity')
        if new_quantity.isdigit():
            item.quantity = int(new_quantity)
            item.save()
        return redirect('staff_inventory')

    return render(request, 'update_inventory.html', {'item': item})
