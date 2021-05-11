#Django
from django.contrib import admin
from django.urls import path, include,re_path
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static

from django.views.static import serve
#Views
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('', HomeView.as_view(), name='home'),
    path('crear_citas/',CrearCitas.as_view(),name='crear_citas'),
    path('eps/', include('UniamigaApp.urls')),
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)