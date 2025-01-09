from django.urls import path,include
# from blog.views import AccountViewset
from rest_framework import routers
from .views import BlogListCreateAPIView,BlogDetailAPIView

# router = routers.SimpleRouter()
# router.register(r'anjali',BlogViewset,basename='user')


urlpatterns = [
   path('blogs/',BlogListCreateAPIView.as_view(),name='blog-list'),
   path('blogs/<int:pk>/',BlogDetailAPIView.as_view(),name='blog-detail'),
    
]
