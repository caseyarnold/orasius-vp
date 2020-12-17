from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from datetime import datetime, timedelta

class ForumCategory(models.Model):
    def __unicode__(self):
        return self.title

    def latest_post(self):
        return ForumTopic.objects.filter(category=self.id).filter(active=True).latest('created_at')
        # reply = ForumReply.order_by('-created_at').select_related().filter(topic__category=self.id).first()

    title = models.TextField(max_length=72)
    body = models.TextField()

class ForumTopic(models.Model):
    class Meta:
        permissions = (
            ("no_wait", "No wait between posting topics"),
        )

    def __unicode__(self):
        return self.title

    def count_replies(self):
        return ForumReply.objects.filter(topic=self.id).filter(active=True).count()

    def count_user_posts(self):
        return ForumTopic.objects.filter(user=self.user).filter(active=True).count() \
               + ForumReply.objects.filter(user=self.user).filter(active=True).count()

    @staticmethod
    def last_posted_at(user):
        try:
            return ForumTopic.objects.filter(user=user).latest('created_at').created_at
        except ForumTopic.DoesNotExist:
            return datetime.now() - timedelta(hours=1)

    @staticmethod
    def user_can_post(user):
        if datetime.now() > (ForumTopic.last_posted_at(user) + timedelta(minutes=10)):
            return True

        return False

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.TextField(max_length=72)
    category = models.ForeignKey(ForumCategory, on_delete=models.CASCADE)
    body = models.TextField(max_length=1200)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class ForumReply(models.Model):
    class Meta:
        permissions = (
            ("no_wait", "No wait between posting replies"),
        )

    def __unicode__(self):
        return self.body

    def count_user_posts(self):
        return ForumTopic.objects.filter(user=self.user).count() + ForumReply.objects.filter(user=self.user).count()

    @staticmethod
    def last_posted_at(user):
        try:
            return ForumReply.objects.filter(user=user).latest('created_at').created_at
        except ForumReply.DoesNotExist:
            return datetime.now() - timedelta(hours=1)

    @staticmethod
    def user_can_post(user):
        if datetime.now() > (ForumReply.last_posted_at(user) + timedelta(seconds=30)):
            return True

        return False

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    topic = models.ForeignKey(ForumTopic, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    body = models.TextField(max_length=1200)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
