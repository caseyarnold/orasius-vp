from django.db import models
from .models import BankAccount
from django.contrib import admin

class BankAccountAdmin(admin.ModelAdmin):
    list_display = ('user', 'cp')
    search_fields = ['user__username', 'user__id', 'user__email']

admin.site.register(BankAccount, BankAccountAdmin)
