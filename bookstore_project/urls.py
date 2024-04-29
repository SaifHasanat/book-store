from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
                      # user management
                      path('admin/', admin.site.urls),
                      # third party
                      path('accounts/', include('allauth.urls')),
                      path('paypal/', include('paypal.standard.ipn.urls')),
                      path('__debug__/', include(debug_toolbar.urls)),
                      # locally
                      path('', include('pages.urls')),
                      path('books/', include('books.urls')),
                      path('orders/', include('orders.urls')),

      ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
