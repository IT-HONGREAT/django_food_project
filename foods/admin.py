from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Menu, Review, User
# Register your models here.

admin.site.register(User, UserAdmin)
UserAdmin.fieldsets += (("Custom fields",
                        {"fields": ("nickname", "profile_img", "intro")}),)

admin.site.register(Review)
admin.site.register(Menu)
