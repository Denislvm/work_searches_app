from django.contrib import admin
from django.urls import path, include
from thesisproject import settings
from searcherapp.views import *
from django.conf.urls.static import static
from django.views.static import serve as mediaserve


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('searcherapp.urls')),
    path('captcha/', include('captcha.urls')),
]


