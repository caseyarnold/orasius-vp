from django.db import models
from auths.models import Profile
from django.contrib import admin
from .models import ForumTopic, ForumCategory, ForumReply

class ForumTopicAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'body', 'created_at', 'updated_at')
    search_fields = ['user__username', 'user__id', 'user__email', 'title', 'body']

class ForumCategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'body')
    search_fields = ['title', 'body']

class ForumReplyAdmin(admin.ModelAdmin):
    list_display = ('user', 'body', 'created_at', 'updated_at', 'topic')
    search_fields = ['user__username', 'user__id', 'user__email', 'body']

admin.site.register(ForumReply, ForumReplyAdmin)
admin.site.register(ForumCategory, ForumCategoryAdmin)
admin.site.register(ForumTopic, ForumTopicAdmin)

