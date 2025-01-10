
from .models import Blog
from .serializers import BlogSerializer
from django.http import HttpResponse

from rest_framework.response import Response

from rest_framework.permissions import IsAuthenticated 
from rest_framework.views import APIView



class BlogPostAPIView(APIView):
    permission_classes = [IsAuthenticated]
    # to retrieve all blog posts
    def get(self, request):
        posts  = Blog.objects.all()
        serializer = BlogSerializer(posts, many=True)
        print(serializer.data)
        return Response(serializer.data)
    
    def post(self,request):
        posts = Blog.objects.all()
        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        return Response(serializer.errors,status=400)


class BlogPostDetailAPIView(APIView):
    permission_classes  = [IsAuthenticated]
    def get_object(self, pk):
        try:
            return Blog.objects.get(pk=pk)
        except Blog.DoesNotExist:
            return HttpResponse(status=404)

    def get(self, request, pk):
        post = self.get_object(pk)
        serializer = BlogSerializer(post)
        return Response(serializer.data)
    
    def put(self, request,pk):
        post = self.get_object(pk)
        serializer = BlogSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=400)
    
    def delete(self, request,pk):
        post = self.get_object(pk)
        post.delete()
        return Response(status=204)





