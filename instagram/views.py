from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Post
from .serializers import PostSerializer
from rest_framework import generics
from rest_framework.decorators import action

class PublicPostListAPIView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
    @action(detail = True, method = ["GET"])
    def public(self, request):
        qs = self.queryset.filter(is_public=True)
        serializer = self.get_serializer(qs, many=True)
        return Response(serializer.data)