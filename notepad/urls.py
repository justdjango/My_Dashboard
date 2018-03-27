
from django.conf.urls import url

from .views import create_view, list_view

urlpatterns = [
    url(r'^create/', create_view, name='create'),
    url(r'^list/', list_view, name='list')
]
