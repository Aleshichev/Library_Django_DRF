from .permissions import UserPermission
from .serializers import CustomUserSerializer
from rest_framework import viewsets
from authentication.models import CustomUser


class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = (UserPermission,)
