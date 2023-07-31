from rest_framework.permissions import BasePermission


class OrderPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method in ["POST"]:
            return request.user.is_authenticated
        elif request.method in ["PUT", "DELETE"]:
            return request.user.is_authenticated
        elif request.method in ["GET"] and "pk" in view.kwargs:
            return request.user.is_authenticated
        elif request.method in ["GET"]:
            return request.user.is_superuser
        return False

    def has_object_permission(self, request, view, obj):
        user = request.user
        return obj.user == user or user.is_staff
