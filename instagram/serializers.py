from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Post 

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['usernam', 'email']

class PostSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()
    class Meta:
        model = Post 
        fields = [
            'pk',
            'author',
            'message',
            'created_at',
            'updated_at'
        ] 