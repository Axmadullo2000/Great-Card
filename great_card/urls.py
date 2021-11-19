from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.urls import include
from store.views import store
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('product.urls')),
    path('store/', include('store.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)