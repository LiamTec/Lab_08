from rest_framework import serializers
from .models import Category, Tag


class CategorySerializer(serializers.ModelSerializer):
    """Serializer for the Category model"""
    class Meta:
        model = Category
        fields = ['id', 'name', 'description']
        read_only_fields = ['id']

class TagSerializer(serializers.ModelSerializer):  
    """Serializer for the Tag model"""
    class Meta:
        model = Tag
        fields = ['id', 'name']
        read_only_fields = ['id']
        