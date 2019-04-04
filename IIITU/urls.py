from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static

from main.views import IndexPageView, HomePageView, PlacementDeskView, ReachView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', IndexPageView.as_view(), name='index'),

    path('i18n/', include('django.conf.urls.i18n')),
    path('home/', HomePageView.as_view(), name='home'),
    path('placementdesk/', PlacementDeskView.as_view(), name='placements'),
    path('reach/', ReachView.as_view(), name='reach'),

    path('accounts/', include('accounts.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
