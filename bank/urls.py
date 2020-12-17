from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^index$', views.index, name='bank_index'),
    url(r'^', views.index, name='bank_index'),
]
