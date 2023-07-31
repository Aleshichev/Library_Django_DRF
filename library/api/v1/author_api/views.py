from rest_framework import viewsets
from .serializers import AuthorSerializer
from rest_framework.permissions import IsAdminUser
from author.models import Author


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = (IsAdminUser,)
