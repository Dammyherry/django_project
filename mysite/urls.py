from django.contrib import admin
from django.urls import path   # 👈 YOU ARE MISSING THIS
from myapp.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
]