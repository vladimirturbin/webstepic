from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('qa/', include('qa.urls')),
    path('admin/', admin.site.urls)
]

