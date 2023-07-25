from django.contrib import admin

from .models import Order


class OrderAdmin(admin.ModelAdmin):
    list_display = (
        "get_book_name",
        "get_user_first_name",
        "created_at",
        "plated_end_at",
        "end_at",
    )

    list_filter = ("created_at", "end_at", "plated_end_at")

    def get_book_name(self, obj):
        return obj.book.name

    get_book_name.short_description = "Book"

    def get_user_first_name(self, obj):
        return obj.user.first_name

    get_user_first_name.short_description = "User_name"


admin.site.register(Order, OrderAdmin)
