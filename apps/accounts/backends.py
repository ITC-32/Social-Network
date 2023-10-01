from django.contrib.auth.backends import BaseBackend
from django.core.exceptions import MultipleObjectsReturned
from django.http import HttpRequest

from apps.accounts.models import CustomUser


class CustomUserAuthentication(BaseBackend):

    def authenticate(
        self, request: HttpRequest,
        email: str = None, password: str = None
    ) -> CustomUser | None:
        if email:
            user = CustomUser.objects.get(email=email)
            can_auth = self.user_can_authenticate(user)
            if not can_auth:
                return
            valid_password = user.check_password(password)
            if not valid_password:
                return
            return user

    def user_can_authenticate(self, user: CustomUser) -> bool:
        return all([getattr(user, 'is_active', False)])

    def get_user(self, user_id: int) -> CustomUser | None:
        try:
            user = CustomUser.objects.get(pk=user_id)
            return user
        except MultipleObjectsReturned:
            return
