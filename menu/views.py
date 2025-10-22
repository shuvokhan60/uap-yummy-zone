from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import FoodItem, Order




def student_menu(request):
    foods = FoodItem.objects.filter(available=True)
    return render(request, 'student_menu.html', {'foods': foods})


@login_required
def order_food(request, item_id):
    food = get_object_or_404(FoodItem, id=item_id)
    order = Order.objects.create(
        user=request.user,
        food_item=food,
        quantity=1,
        total_price=food.price
    )
    messages.success(request, f"✅ You have ordered {food.name} successfully!")
    return redirect('student_orders')


@login_required
def student_orders(request):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'student_orders.html', {'orders': orders})


@login_required
def make_payment(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    order.is_paid = True
    order.save()
    messages.success(request, "💳 Payment successful! Thank you!")
    return redirect('student_orders')




@login_required
def staff_menu(request):
    foods = FoodItem.objects.all().order_by('-id')
    return render(request, 'staff_menu.html', {'foods': foods})


@login_required
def add_food(request):
    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']
        price = request.POST['price']
        image = request.FILES.get('image')

        FoodItem.objects.create(
            name=name,
            description=description,
            price=price,
            image=image
        )
        messages.success(request, "🍔 New food added successfully!")
        return redirect('staff_menu')

    return render(request, 'add_food.html')


@login_required
def edit_food(request, food_id):
    food = get_object_or_404(FoodItem, id=food_id)

    if request.method == 'POST':
        food.name = request.POST.get('name')
        food.description = request.POST.get('description')
        food.price = request.POST.get('price')
        food.quantity = request.POST.get('quantity', 0)
        food.available = 'available' in request.POST

        if 'image' in request.FILES:
            food.image = request.FILES['image']

        food.save()
        messages.success(request, "✅ Food updated successfully!")
        return redirect('staff_menu')

    return render(request, 'edit_food.html', {'food': food})


@login_required
def delete_food(request, food_id):
    food = get_object_or_404(FoodItem, id=food_id)
    food.delete()
    messages.warning(request, "🗑️ Food deleted successfully!")
    return redirect('staff_menu')




@login_required
def manage_orders(request):
   
    orders = Order.objects.select_related('user', 'food_item').order_by('-created_at')
    return render(request, 'manage_orders.html', {'orders': orders})


@login_required
def update_order_status(request, order_id):
   
    order = get_object_or_404(Order, id=order_id)
    order.is_paid = not order.is_paid
    order.save()
    messages.info(request, f"🔄 {order.food_item.name} order status updated!")
    return redirect('manage_orders')
@login_required
def update_quantity(request, food_id):
    food = get_object_or_404(FoodItem, id=food_id)

    if request.method == 'POST':
        new_quantity = request.POST.get('quantity')
        if new_quantity.isdigit():
            food.quantity = int(new_quantity)
            food.save()
            messages.success(request, f"✅ Quantity for {food.name} updated to {food.quantity}.")
        else:
            messages.error(request, "❌ Invalid quantity value.")

    return redirect('staff_menu')
