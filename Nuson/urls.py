from django.contrib import admin
from django.urls import path, include
# from dashboard.admin import nuson_site

urlpatterns = [
    path('', include('dashboard.urls')),
    path('', include('api.urls')),
    path('admin/', admin.site.urls),
    # path('nusonadmin/', nuson_site.urls),
]
