
from django.contrib import admin
from django.urls import path
from deathcore import views as deathcore_views
from portfolio import views as  portfolio_views
from django.conf import settings

urlpatterns = [ 
    path('admin/', admin.site.urls),
    path('', deathcore_views.home, name="home"),
    path('about/', deathcore_views.about, name="about"),
    path('contact/', deathcore_views.contact, name="contact"),
    path('portfolio/', portfolio_views.portfolio, name="portfolio"),
    
]
#Validar el DEBUG
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)