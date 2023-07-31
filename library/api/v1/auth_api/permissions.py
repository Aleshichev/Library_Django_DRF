from rest_framework.permissions import BasePermission


class UserPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method in ["POST"]:
            return True
        elif request.method in ["PUT", "DELETE"]:
            return request.user.is_authenticated or request.user.is_superuser
        elif request.method in ["GET"] and "pk" in view.kwargs:
            return request.user.is_authenticated
        elif request.method in ["GET"]:
            return request.user.is_superuser
        return False

    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return obj
        if request.user.is_authenticated:
            return obj == request.user
