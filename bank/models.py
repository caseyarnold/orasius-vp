from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from auths.models import Profile


class BankAccount(models.Model):
    def deposit(self, user, amount):
        user_profile = Profile.objects.get(user=user)
        bank_account = BankAccount.objects.get(user=user)

        if (user_profile is None or bank_account is None):
            return False

        if( user_profile.cp >= amount):
            user_profile.cp -= amount
            user_profile.save()

            bank_account.cp += amount
            bank_account.save()

            return True

        return False

    def withdraw(self, user, amount):
        user_profile = Profile.objects.get(user=user)
        bank_account = BankAccount.objects.get(user=user)

        if (user_profile is None or bank_account is None):
            return False

        if ( amount <= bank_account.cp):
            user_profile.cp += amount
            user_profile.save()

            bank_account.cp -= amount
            bank_account.save()

            return True

        return False

    def __unicode__(self):
       return self.user.username

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cp = models.BigIntegerField(default=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
