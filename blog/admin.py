from django.contrib import admin

from .models import user

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_filter = ("name", "email")
    list_display = ("name", "email", "password")

admin.site.register(user, UserAdmin)
