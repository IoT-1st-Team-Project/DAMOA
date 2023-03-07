
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include('main.urls')),  # / 페이지에 해당하는 urlpatterns 
    path('common/', include('common.urls')),
]

