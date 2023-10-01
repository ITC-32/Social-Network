from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.hashers import make_password


class CustomUserManager(BaseUserManager):

    def create_user(self, email: str, password: str, **other_params):
        normalized_email = self.normalize_email(email)
        hashed_password = make_password(password)
        user = self.model(
            email=normalized_email,
            password=hashed_password,
            **other_params
        )
        user.save(using=self._db)
        return user

    def create_superuser(self, email: str, password: str, **other_params):
        extra_data = {
            'is_superuser': True,
            'is_staff': True
        }
        other_params.update(extra_data)
        user = self.create_user(email, password, **other_params)
        return user
