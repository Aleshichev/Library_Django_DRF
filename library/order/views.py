from .models import Order
from django.shortcuts import render, redirect
from datetime import datetime
from django.contrib import messages
from .forms import OrderForm
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

from .serializers import OrderListSerializer, OrderCreateSerializer, OrderUserSerializer
from .permissions import OrderPermission


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
        form = OrderForm()

    return render(request, "order/create_order.html", {"form": form})


def close_order(request, order_id):
    order = Order.get_by_id(order_id)

    if order:
        order.update(end_at=datetime.now())

    return redirect("order:order")


class OrderUserViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderListSerializer
    permission_classes = (IsAdminUser,)

    def get_queryset(self):
        user_id = self.kwargs["user_id"]
        return self.queryset.filter(user_id=user_id)

    def get_serializer_class(self):
        if self.action in ["create", "update", "partial_update"]:
            return OrderUserSerializer
        return OrderListSerializer


class OrderViewSet(
    viewsets.mixins.CreateModelMixin,
    viewsets.mixins.RetrieveModelMixin,
    viewsets.mixins.UpdateModelMixin,
    viewsets.mixins.DestroyModelMixin,
    viewsets.mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Order.objects.all()
    serializer_class = OrderListSerializer
    permission_classes = (OrderPermission,)

    def get_serializer_class(self):
        if self.request.method == "GET":
            return OrderListSerializer
        else:
            return OrderCreateSerializer
