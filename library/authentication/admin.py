from django.contrib import admin
from .models import CustomUser


class CustomUserAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "is_superuser",
        "first_name",
        "last_name",
        "middle_name",
        "email",
        "password",
        "created_at",
        "updated_at",
        "role",
        "is_active",
        "is_staff",
    )

    def save_model(self, request, obj, form, change):
        if not change or not obj.has_usable_password():
            obj.set_password(form.cleaned_data["password"])
        super().save_model(request, obj, form, change)


admin.site.register(CustomUser, CustomUserAdmin)
