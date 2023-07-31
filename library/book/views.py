from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Book
from .models import Author
from authentication.models import CustomUser
from order.models import Order
from django.utils.datastructures import MultiValueDictKeyError
from .forms import AddFormBook, FilterForm, AddUserForm, AddAuthorForm


@login_required
def books_page(request):
    filter_form = FilterForm(request.POST or None)
    add_user_form = AddUserForm(request.POST or None)
    add_book_form = AddFormBook(request.POST or None)

    if filter_form.is_valid():
        parameter = filter_form.cleaned_data["parameter"]
        value = filter_form.cleaned_data["value"]

        if parameter == "None" or not value:
            books = Book.objects.all()
        elif parameter == "authors":
            books = Book.objects.filter(authors=value)
        elif parameter == "title":
            books = Book.objects.filter(name=value)
        elif parameter == "count":
            books = Book.objects.filter(count=value)
    else:
        books = Book.objects.all()

    return render(
        request,
        template_name="book/basik.html",
        context={
            "books": books,
            "filter_form": filter_form,
            "add_user_form": add_user_form,
            "add_book_form": add_book_form,
            "user": CustomUser.objects.all(),
        },
    )


def book_add_page(request):
    filter_form = FilterForm(request.POST or None)
    add_user_form = AddUserForm(request.POST or None)
    add_book_form = AddFormBook(request.POST or None)
    user = CustomUser.objects.all
    book = Book.objects.all()
    try:
        if request.POST["user"]:
            all_order = Order.objects.all()
            book = []
            for elem in all_order:
                if elem.user.id == int(request.POST["user"]):
                    book.append(elem.book)
    except MultiValueDictKeyError:
        book = Book.objects.all()
    return render(
        request,
        template_name="book/basik.html",
        context={
            "books": book,
            "user": user,
            "filter_form": filter_form,
            "add_user_form": add_user_form,
            "add_book_form": add_book_form,
        },
    )


@login_required
def book_detail(request, book_id):
    authors = Author.objects.all()
    book = Book.objects.get(id=book_id)
    book_authors = book.authors.all()

    if request.method == "POST":
        form = AddAuthorForm(request.POST)
        if form.is_valid():
            author = form.cleaned_data["author"]
            book.authors.add(author)
            book.save()
    else:
        form = AddAuthorForm()
    return render(
        request,
        template_name="book/book.html",
        context={
            "book": Book.get_by_id(book_id),
            "authors": authors,
            "book_authors": book_authors,
            "form": form,
        },
    )


def add_book(request):
    if request.method == "POST":
        form = AddFormBook(request.POST)
        if form.is_valid():
            form.save()
            return books_page(request)
    else:
        form = AddFormBook()
    return render(
        request,
        template_name="book/add_book.html",
        context={"form": form, "authors": Author.objects.all()},
    )
