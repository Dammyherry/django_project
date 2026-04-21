from django.contrib import admin
from django.urls import path
from myapp.views import home   # 👈 import your view directly

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),   # 👈 direct connection (no include needed)
]