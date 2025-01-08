from rest_framework import serializers
from blog.models import Blog    

class BlogSerializer(serializers.Serializer):
    created_at = serializers.DateTimeField()
    title = serializers.CharField(max_length=100)
    content = serializers.CharField()


 

