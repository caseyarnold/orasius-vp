from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

class UserMessage(models.Model):

    def __unicode__(self):
        return self.title

    from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='from_user')
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='to_user')
    title = models.TextField(max_length=100)
    body = models.TextField(max_length=1200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)