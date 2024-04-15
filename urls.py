from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from MadeWithLove.commons import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomePage.as_view(), name='home'),
    path('account/', include('MadeWithLove.accounts.urls')),
    path('ad/', include('MadeWithLove.ads.urls')),
    path('order/', include('MadeWithLove.orders.urls'))
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)