from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

from apps.accounts.models import CustomUser


class CreateCustomUserForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('email',)


class ChangeCustomUserForm(ModelForm):

    class Meta:
        model = CustomUser
        fields = ('email', 'password',)
