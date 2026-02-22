from django.db import models

# Create your models here.
from django.contrib.auth.models import User


class Post(models.Model):
    """
    Post model represents a blog post.

    Fields:
    - title: Title of the blog post
    - content: Main body of the blog
    - published_date: Automatically set when created
    - author: The user who created the post
    """

    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts'
    )

    def __str__(self):
        return self.title
