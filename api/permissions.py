from django.contrib.auth import get_user_model
from rest_framework.permissions import SAFE_METHODS, BasePermission

User = get_user_model()


class IsAdmin(BasePermission):
    allowed_user_roles = ('admin',)

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            if (request.user.role in self.allowed_user_roles
                    or request.user.is_staff):
                return True
        return False


class IsModerator(BasePermission):
    allowed_user_roles = ('moderator',)

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            if request.user.role in self.allowed_user_roles:
                return True
        return False


class IsUser(BasePermission):
    allowed_user_roles = ('user',)

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            if request.user.role in self.allowed_user_roles:
                return True
        return False


class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_authenticated:
            return obj.author == request.user
        else:
            return False


class IsAdminUserOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        elif request.user.is_authenticated:
            return (request.user.is_staff
                    or request.user.role == 'admin')
        else:
            return False


class ReviewCommentPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        else:
            return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        allowed_user_roles = ('admin', 'moderator')

        return (request.method in SAFE_METHODS
                or obj.author == request.user
                or request.user.role in allowed_user_roles)
