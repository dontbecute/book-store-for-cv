from django.contrib import admin

# Register your models here.
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

# this is local class import from form.py file ...
from .forms import UserChange, UserCreation

CustomUser = get_user_model()

class CustomAdmin(UserAdmin):
        model = get_user_model()
        add_form = UserCreation
        form = UserChange

        list_display = [
            "first_name",
            "email",
            "username",
            "is_superuser",

        ]


admin.site.register(CustomUser ,CustomAdmin)
