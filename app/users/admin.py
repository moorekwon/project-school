from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group
from django.contrib.sites.models import Site

from users.models import Student

User = get_user_model()


class UserAdmin(BaseUserAdmin):
    add_fieldsets = (
        (None, {
            'fields': ('email', 'username', 'is_student', 'is_teacher', 'password1', 'password2')
        }),
        ('Permissions', {
            'fields': ('is_superuser', 'is_staff')
        })
    )

    fieldsets = (
        (None, {
            'fields': ('email', 'username', 'is_student', 'is_teacher', 'password',)
        }),
        ('Permissions', {
            'fields': ('is_superuser', 'is_staff',)
        })
    )

    list_display = ['email', 'username', 'is_student', 'is_teacher', ]
    search_fields = ('email', 'username',)
    ordering = ('email',)


admin.site.register(Student)
admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
admin.site.unregister(Site)
