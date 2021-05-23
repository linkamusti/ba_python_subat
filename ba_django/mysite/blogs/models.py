from django.db import models

# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=20, default="title")
    text = models.TextField(max_length=300)
    author = models.CharField(max_length=50)
    publish_date = models.DateTimeField('date published')
    avg_rating = models.FloatField()

    def __str__(self):
        return self.title


class Comment(models.Model):
    text = models.TextField(max_length=100)
    username = models.CharField(max_length=50)
    rating = models.FloatField()

    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
