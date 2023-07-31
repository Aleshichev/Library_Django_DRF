from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Author
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from book.models import Book
from .forms import AuthorForm


class AuthorPage(ListView):
    template_name = "author/author.html"
    model = Author
    context_object_name = "authors"
    ordering = "surname"


class AuthorDetails(DetailView):
    template_name = "author/author_details.html"
    context_object_name = "author"
    model = Author

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        author = self.get_object()
        context["books"] = Book.objects.filter(authors=author)
        return context


def remove_author(request, author_id):
    if request.method == "POST":
        try:
            author = Author.objects.get(pk=author_id)
            books_authors = Book.objects.filter(authors=author)
        except Author.DoesNotExist:
            raise Http404("Question does not exist")
        if len(books_authors) == 0:
            author.delete()
        return HttpResponseRedirect(reverse("author:author"))


def add_author(request):
    if request.method == "POST":
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("author:author"))
    else:
        form = AuthorForm()
    return render(request, "author/author_create.html", {"form": form})
