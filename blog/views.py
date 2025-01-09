from django.shortcuts import render
from .models import Blog
from .serializers import BlogSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from rest_framework.parsers import JSONParser

from rest_framework.response import Response
from rest_framework import viewsets


blogs  = []
b1 = Blog(created_at='2018-01-01', title='Blog 1', content='This is blog 1')
b2= Blog(created_at='2018-01-02', title='Blog 2', content='This is blog 2')

blogs.append(b1)
blogs.append(b2)

    

class BlogViewset(viewsets.ReadOnlyModelViewSet):
    
    queryset = Blog.objects.all()
    def list(self, request):

        print("hello there")
        serializer = BlogSerializer(blogs ,many=True)  
        json_data = JSONRenderer().render(serializer.data)
        print("json" ,json_data)
        return Response(json_data)
    

