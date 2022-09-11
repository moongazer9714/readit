from django.db import models

# Create your models here.


class FeedBack(models.Model):
    name = models.CharField(max_length=222)
    position = models.CharField(max_length=222)
    avatar = models.ImageField(upload_to='about/')
    context = models.TextField()

    def __str__(self):
        return self.name