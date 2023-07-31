from .permissions import IsAdminOrReadOnly
from rest_framework import generics
from .serializers import BookSerializer, BookListSerializer
from book.models import Book


class BookRetrieveApiList(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = (IsAdminOrReadOnly,)


class BookApiList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookListSerializer
    permission_classes = (IsAdminOrReadOnly,)


class BookApiCreate(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = (IsAdminOrReadOnly,)