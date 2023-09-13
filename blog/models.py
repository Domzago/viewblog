from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    intro = models.TextField()
    content = models.TextField()
    posted = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-posted']

    def __str__(self) -> str:
        return self.title

class Profile(models.Model):
    username = models.CharField(max_length=200)
    email = models.EmailField()
    password1 = models.CharField(max_length=200)
    password2 = models.CharField(max_length=200)