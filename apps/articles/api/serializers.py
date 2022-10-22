from rest_framework import serializers
from apps.articles.models import Article


class ArticleGetSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source='category.title', read_only=True)

    class Meta:
        model = Article
        fields = ['id', 'category', 'title', 'get_image_url', 'context', 'tags', 'views', 'created_at']


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['category', 'title', 'image', 'context', 'tags', 'views', 'created_at']
        extra_kwargs = {
            'views': {'read_only': True}
        }