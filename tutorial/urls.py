
from django.contrib import admin
from django.urls import path,include

from . import views
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("app_1.urls")),
    path("",views.home)
]
