from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin

from finance.views import company_article_list, ChartData, dash, dash_ajax

from news.views import scrape
from .views import home


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^notes/', include('notepad.urls', namespace='notes')),
    url(r'^scrape/', scrape, name='scrape'),
    url(r'^home/', home, name='home'),
    url(r'^companies/', company_article_list, name='companies'),
    url(r'^api/chart/data/$', ChartData.as_view(), name='api-chart-data'),
    url(r'^dash/', dash),
    url(r'^_dash', dash_ajax)
    
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
