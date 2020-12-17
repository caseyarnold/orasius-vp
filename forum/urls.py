"""codebase URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='forum_homepage'),
    url(r'^topics\/([0-9]+)\/create$', views.create_topic, name='forum_create_topic'),
    url(r'^topic\/([0-9]+)\/page-([0-9]+)$', views.view_topic, name='forum_view_topic'),
    url(r'^topics\/([0-9]+)\/page-([0-9]+)$', views.list_topics, name='forum_list_topics'),
]
