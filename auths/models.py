from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    def __unicode__(self):
        return self.user.username

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cp = models.BigIntegerField(default=1000)
    credits = models.BigIntegerField(default=10)
    last_seen = models.DateTimeField(auto_now=True)
    avatar = models.IntegerField()
    forum_banned = models.BooleanField(default=False)
    forum_banned_reason = models.TextField(null=True)
    forum_banned_lifted = models.DateTimeField(null=True)