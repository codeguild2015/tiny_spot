from django.contrib import admin
from .forms import SignUpForm
from .models import SignUp


class SignUpAdmim(admin.ModelAdmin):
    """Allows us to customize how admin works"""
    list_display = ["__unicode__", "timestamp", "updated"]
    form = SignUpForm

admin.site.register(SignUp, SignUpAdmim)
