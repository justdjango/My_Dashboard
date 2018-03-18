
from django.conf.urls import url

from .views import createView

urlpatterns = [
    url(r'^create', createView, name='create'),
]
