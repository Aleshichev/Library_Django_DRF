from rest_framework import serializers
from book.models import Book
from api.v1.author_api.serializers import AuthorSerializer


class BookListSerializer(serializers.ModelSerializer):
    authors = AuthorSerializer(many=True)

    class Meta:
        model = Book
        fields = "__all__"


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"
