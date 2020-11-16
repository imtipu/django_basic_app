from django.contrib import admin
# from django.contrib.auth.admin import
from django.contrib.auth import admin as auth_admin

# Register your models here.
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

User = get_user_model()


@admin.register(User)
class UssrAdmin(auth_admin.UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
