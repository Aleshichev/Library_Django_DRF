from rest_framework import serializers
from .models import Order
from api.v1.book_api.serializers import BookSerializer
from api.v1.auth_api.serializers import CustomUserforOrderSerializer


class OrderListSerializer(serializers.ModelSerializer):
    book = BookSerializer()
    user = CustomUserforOrderSerializer()

    class Meta:
        model = Order
        fields = "__all__"


class OrderCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['book', 'plated_end_at']

    def save(self, **kwargs):
        user = self.context['request'].user
        self.validated_data['user'] = user
        return super().save(**kwargs)
    

class OrderUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = "__all__"
