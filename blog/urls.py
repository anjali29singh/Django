from django.urls import path,include
from blog.views import BlogViewset
# from blog.views import AccountViewset
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'anjali',BlogViewset,basename='user')


urlpatterns = [

   # path('',views.home,name='blog-home') 


   path('',include(router.urls)),
   # explicitely url config 
   # path('',BlogViewset.as_view({'get':'list'}))
    
]
