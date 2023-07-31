from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser
from order.models import Order
from .serializers import OrderListSerializer, OrderCreateSerializer, OrderUserSerializer
from .permissions import OrderPermission


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
