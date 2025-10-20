from django.shortcuts import render, redirect, get_object_or_404
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
    return redirect('student_orders')


@login_required
def student_orders(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'student_orders.html', {'orders': orders})


def make_payment(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    order.is_paid = True
    order.save()
    return redirect('my_orders')
