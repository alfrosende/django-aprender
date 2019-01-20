from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import OpusUser
from django.contrib.auth.models import User

class UserInline(admin.StackedInline):
    model = OpusUser
    can_delete = False
    verbose_name_plural = "Usuarios opus"

class UserAdmin(UserAdmin):
    inlines = (UserInline, )

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(OpusUser)
