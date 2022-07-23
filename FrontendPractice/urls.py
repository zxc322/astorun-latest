from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    path('admin/', admin.site.urls),

] + i18n_patterns(
    path('i18n/', include('django.conf.urls.i18n')),
    path('shop/', include('product.urls')),
    path('contacts/', include('contacts.urls')),
    path('bookmarks/', include('bookmarks.urls')),
    path('news/', include('news.urls')),
    path('', include('mainFront.urls')),
    path('collection/', include('collection.urls')),
    path('order/', include('order.urls')),
    prefix_default_language=False,
)

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
