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
from django.conf.urls import url, include
from django.contrib import admin
from main import views
# title for admin site
admin.site.site_header = 'Orasius Admin'

urlpatterns = [
    url(r'^auth/', include('auths.urls')),
    url(r'^bank/', include('bank.urls')),
    url(r'^forum/', include('forum.urls')),
    url(r'^messages/', include('user_messages.urls')),
    url(r'^$', views.home, name='homepage'),
    url(r'^profile\/(.*)$', views.profile, name='user_profile'),
    url(r'^leadminpanel/', admin.site.urls, name='admin_panel'),

]
