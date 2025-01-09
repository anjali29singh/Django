from rest_framework import serializers
from blog_api.models import Blog   

class BlogSerializer(serializers.Serializer):
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()
    title = serializers.CharField(max_length=100)
    content = serializers.CharField()


 
