from django.db import models
from .models import Profile
from django.contrib import admin
from django.contrib.auth.models import Permission


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'cp', 'credits')
    search_fields = ['user__username', 'user__id', 'user__email']

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Permission)
