from django.conf.urls.static import static
from django.urls import path

from config.settings import base
from notify.admin import admin_site


urlpatterns = [
    path('admin/', admin_site.urls),

] + static(base.STATIC_URL, document_root=base.STATIC_ROOT)
