from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'content', 'image', 'author', 'created_at', 'updated_at']
        read_only_fields = ['author', 'created_at', 'updated_at']
