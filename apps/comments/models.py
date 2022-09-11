from django.db import models
from apps.articles.models import Article


# Create your models here.


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    name = models.CharField(max_length=222)
    avatar = models.ImageField(upload_to='comments/', null=True, blank=True)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
