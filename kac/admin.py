from django.contrib import admin

# Register your models here.
from .models import UpdatedUser

class UpdatedUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'my_key']

admin.site.register(UpdatedUser, UpdatedUserAdmin)