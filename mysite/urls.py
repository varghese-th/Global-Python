
from django.conf.urls import url,include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('home.urls')),
    url(r'^about/', include('about.urls')),
    url(r'^cctv/', include('cctv.urls')),
    url(r'^accessories/', include('accessories.urls')),
    url(r'^mobile/', include('mobile.urls')),
    url(r'^automation/', include('automation.urls')),
    url(r'^alarm/', include('alarm.urls')),
    url(r'^biometric/', include('biometric.urls')),
    url(r'^gps/', include('gps.urls')),
    url(r'^stickers/', include('stickers.urls')),
    url(r'^enquiry/', include('enquiry.urls')),
    url(r'^contact/', include('contact.urls')),
   
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)