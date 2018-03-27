
from django.conf.urls import url

from .views import create_view, list_view, delete_view

urlpatterns = [
    url(r'^create/', create_view, name='create'),
    url(r'^list/', list_view, name='list'),
    url(r'^(?P<id>\d+)/delete/', delete_view, name='delete'),
]
