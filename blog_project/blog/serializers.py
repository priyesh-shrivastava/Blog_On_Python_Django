from rest_framework import serializers
from .models import Post, Category, Comment, Liked

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class LikedSerializer(serializers,ModelSerializer):
    class Meta:
        model = Liked
        fields = '__all__'