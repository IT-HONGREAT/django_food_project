from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Review, User, Comment
# Register your models here.

admin.site.register(User, UserAdmin)
UserAdmin.fieldsets += (("Custom fields",
                        {"fields": ("nickname", "profile_img", "intro")}),)

class ReviewComment(admin.StackedInline):
    model = Comment
    extra = 0

class ReviewAdmin(admin.ModelAdmin):
    inlines = [
        ReviewComment,
    ]
admin.site.register(Review,ReviewAdmin)
