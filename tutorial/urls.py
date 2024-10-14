from django.urls import path,include
from django.http import HttpResponse
from django.contrib import admin
from users import views as user_views
from django.contrib.auth import views as auth_views
urlpatterns = [

    path('',include('blog.urls')),
    path('register/',user_views.register,name='register'),
    path('login/',auth_views.LoginView.as_view(template_name = 'users/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(next_page='login',http_method_names=['get','post']),name='logout'),
    path('admin/',admin.site.urls)
]
