from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin

from finance.views import company_article_list

from news.views import scrape, news_list


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^notes/', include('notepad.urls', namespace='notes')),
    url(r'^scrape/', scrape, name='scrape'),
    url(r'^home/', news_list, name='home'),
    url(r'^companies/', company_article_list, name='companies')
    
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
