from django.urls import path,include
from .views import BlogPostAPIView, BlogPostDetailAPIView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    
   path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
   path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
   path('posts/',BlogPostAPIView.as_view(),name='posts'),
   path('posts/<int:pk>/',BlogPostDetailAPIView.as_view(),name='post_detail'),
]
