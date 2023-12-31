from .models import Order
from book.models import Book
from django.shortcuts import render, redirect
from datetime import datetime
from django.contrib import messages
from .forms import OrderForm
from django.core.exceptions import ValidationError


def order_list(request):
    orders = Order.objects.order_by("user__id")
    return render(request, "order/order.html", {"orders": orders})


def user_orders(request):
    current_user = request.user
    orders = Order.objects.filter(user=current_user)
    return render(request, "order/user_orders.html", {"orders": orders})


def create_order(request):
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save_order(request.user)
            messages.success(request, "Order placed!")
        else: 
            print(form.errors)
    else:
        form = OrderForm()

    return render(request, "order/create_order.html", {"form": form})


def close_order(request, order_id):
    order = Order.get_by_id(order_id)
    book = Book.objects.get(name=order.book.name)

    if order:
        order.update(end_at=datetime.now())
        book.count += 1
        book.save()

    return redirect("order:order")
