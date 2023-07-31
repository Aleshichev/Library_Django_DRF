"""library URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from authentication.views import HomePageView

from api.v1.author_api.views import AuthorViewSet
from api.v1.auth_api.views import UserViewSet

from api.v1.book_api.views import BookApiList, BookRetrieveApiList, BookApiCreate
from order.views import OrderViewSet, OrderUserViewSet

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r"author", AuthorViewSet)
router.register(r"user", UserViewSet)
router.register(r"order", OrderViewSet)
router.register(r"user/(?P<user_id>\d+)/order", OrderUserViewSet)


urlpatterns = [
    path("", HomePageView.as_view(), name="index"),
    path("home/", include("authentication.urls")),
    path("author/", include("author.urls")),
    path("book/", include("book.urls")),
    path("order/", include("order.urls")),
    path("admin/", admin.site.urls),
    path("api/v1/", include(router.urls)),
    path("api/v1/book/", BookApiList.as_view(), name="book_list"),
    path("api/v1/book/<int:pk>/", BookRetrieveApiList.as_view(), name="book_ret"),
    path("api/v1/book/create/", BookApiCreate.as_view(), name="create"),
    path("api/v1/auth/", include("djoser.urls")),
    re_path(r"^auth/", include("djoser.urls.authtoken")),
]
