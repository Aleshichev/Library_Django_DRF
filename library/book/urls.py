from django.urls import path
from . import views


app_name = "book"


urlpatterns = [
    path("", views.books_page, name="book_main_page"),
    path("<int:book_id>/", views.book_detail, name="book_detail"),
    path("add_book/", views.add_book, name="add_book"),
    path("book_add_page/", views.book_add_page, name="book_add_page"),
]
