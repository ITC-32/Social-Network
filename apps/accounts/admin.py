from django.contrib import admin
from django.contrib.auth.models import Group

from apps.accounts.forms import ChangeCustomUserForm, CreateCustomUserForm
from apps.accounts.models import CustomUser


@admin.register(CustomUser)
class ModelNameAdmin(admin.ModelAdmin):
    form = ChangeCustomUserForm
    add_form = CreateCustomUserForm
    model = CustomUser
    readonly_fields = ['password']


admin.site.unregister(Group)
