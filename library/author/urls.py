from django.urls import path
from . import views
from library.functions import deny_non_librarian


app_name = 'author'

urlpatterns = [
    path("", deny_non_librarian(views.AuthorPage.as_view()), name='author'),
    path("<int:pk>", deny_non_librarian(views.AuthorDetails.as_view()), name='details'),
    path("<int:author_id>/remove", deny_non_librarian(views.remove_author), name='remove_author'),
    path("new/", deny_non_librarian(views.add_author), name='add_author'),
]
