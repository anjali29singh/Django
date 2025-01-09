from django.shortcuts import render
from .models import Blog
from .serializers import BlogSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from rest_framework.parsers import JSONParser

from rest_framework.response import Response
from rest_framework import generics


# List and Create Blogs
class BlogListCreateAPIView(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

# Retrieve, Update, and Delete a Blog
class BlogDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

