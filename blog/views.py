from django.shortcuts import render
from .models import Blog
from .serializers import BlogSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from rest_framework.parsers import JSONParser

# blogs  = []
# b1 = Blog(created_at='2018-01-01', title='Blog 1', content='This is blog 1')
# b2= Blog(created_at='2018-01-02', title='Blog 2', content='This is blog 2')

# blogs.append(b1)
# blogs.append(b2)

def home(request):
    bl = Blog.objects.all()
    serializer = BlogSerializer(blogs, many=True)  
    json_data = JSONRenderer().render(serializer.data)
    print("json" ,json_data)
    return HttpResponse(json_data, content_type='application/json')
    
