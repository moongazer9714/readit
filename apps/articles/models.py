from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=222)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title


class Tag(models.Model):
    title = models.CharField(max_length=222)

    def __str__(self):
        return self.title


class Article(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=222)
    image = models.ImageField(upload_to='articles/')
    context = models.TextField()
    tags = models.ManyToManyField(Tag)
    views = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

