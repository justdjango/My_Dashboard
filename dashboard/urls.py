
from django.conf.urls import url, include
from django.contrib import admin

from news.views import scrape

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^notes/', include('notepad.urls', namespace='notes')),
    url(r'^scrape/', scrape)
]
