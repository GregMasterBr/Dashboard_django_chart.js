from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', include('minha_dashboard.urls',namespace='app_minha_dashboard')),
    path('', include('minha_dashboard.urls')),
    #path('encurtadordelink', include('encurtador.urls',namespace='encurtador')),
    #path('encurtadordelink', include('encurtador.urls')),
    path('encurtadordelink/', include('encurtador.urls',namespace='encurtador')),


]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)