from django.urls import path,include
from django.http import HttpResponse
from django.contrib import admin
urlpatterns = [

    path('',include('home.urls')),
    path('blog/',include('blog.urls')),
    path('admin/',admin.site.urls)
]
