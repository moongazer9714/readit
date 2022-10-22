from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .serializers import ArticleSerializer, ArticleGetSerializer
from ..models import Article


@api_view(["GET"])
def article_list(request):
    if request.method == "GET":
        queryset = Article.objects.all()
        serializer = ArticleGetSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["POST"])
def article_create(request):
    if request.method == "POST":
        data = request.data
        serializer = ArticleSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({"detail": "credential are not valid"}, status=status.HTTP_400_BAD_REQUEST)