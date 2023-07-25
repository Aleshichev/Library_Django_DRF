from django.urls import path
from . import views
from utils import deny_non_librarian


app_name = "authentication"

urlpatterns = [
    path("", views.HomePageView.as_view(), name="index"),
    path("register/", views.registration, name="registration"),
    path("login/", views.LoginPage.as_view(), name="login"),
    path("authentication/", views.user_page, name="user_page"),
    path("out/", views.out, name="log_out"),
    path("users/", deny_non_librarian(views.users_page), name="all_users"),
    path(
        "user/<int:user_id>",
        deny_non_librarian(views.user_details),
        name="special_user",
    ),
]
