from django.contrib import admin

from .models import Book


class BookAdmin(admin.ModelAdmin):
    filter_horizontal = ["authors"]
    list_display = (
        "get_book_id",
        "name",
        "description",
        "count",
        "year_of_publication",
        "date_of_issue",
    )
    # fields = [
    #     ("name", "description"),
    #     "count",
    #     "authors",
    #     "year_of_publication",
    #     "date_of_issue",
    # ]
    list_filter = ("id", "name", "authors__surname")
    fieldsets = [
        (
            "Not change",
            {
                "fields": [("name", "count"), "description", "year_of_publication"],
            },
        ),
        (
            "Change",
            {
                "fields": ["date_of_issue"],
            },
        ),
        (
            "Get_author",
            {
                "fields": ["authors"],
            },
        ),
    ]

    def get_book_id(self, obj):
        return obj.id

    get_book_id.short_description = "Book id"

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return self.readonly_fields + ("name", "count", "description", "year_of_publication")
        return self.readonly_fields


admin.site.register(Book, BookAdmin)
