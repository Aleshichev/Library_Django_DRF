# Create your views here.
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic.base import TemplateView
from .models import CustomUser
from django.contrib.auth import authenticate, login, logout
from django.db.utils import IntegrityError
from order.models import Order
from .forms import LoginForm, RegisterForm


class HomePageView(TemplateView):
    template_name = "authentication/index.html"


class RegisterPage(TemplateView):
    template_name = "authentication/register.html"


class LoginPage(TemplateView):
    template_name = "authentication/login.html"


def user_page(request):
    if request.user.is_authenticated:
        return render(request, template_name="authentication/index.html")
    elif request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():
            user = authenticate(
                request,
                email=form.cleaned_data["email"],
                password=form.cleaned_data["password"],
            )

            if user is not None:
                login(request, user)
                return render(request, template_name="authentication/index.html")
            else:
                return HttpResponse("Error")
    else:
        form = LoginForm()
    return render(request, "authentication/login.html", {"form": form})


def registration(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            role = form.cleaned_data["role"]

            try:
                if role == "0":
                    user = CustomUser.objects.create_user(
                        email=email, password=password, role=role
                    )
                    user.save()
                elif role == "1":
                    user = CustomUser.objects.create_superuser(
                        email=email, password=password, role=role
                    )
                    user.save()
            except IntegrityError:
                return render(
                    request,
                    template_name="authentication/register.html",
                    context={
                        "error_message": "User with that email is already exist, please change email"
                    },
                )
            return redirect("authentication:login")
        else:
            return render(
                request,
                template_name="authentication/register.html",
                context={"form": form},
            )
    else:
        form = RegisterForm()
    return render(
        request,
        template_name="authentication/register.html",
        context={"form": form},
    )


def out(request):
    logout(request)
    return redirect("authentication:login")


def users_page(request):
    users = CustomUser.objects.order_by("id")
    return render(request, "authentication/all_users.html", {"users": users})


def user_details(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    orders = Order.objects.filter(user_id=user_id)
    return render(
        request, "authentication/user_details.html", {"user": user, "orders": orders}
    )
