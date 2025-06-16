from django.db import models
from  django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    is_admin = models.BooleanField(default=False)


class Article(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='Articles')
    title = models.CharField(max_length=60)
    description = models.TextField(max_length=400)
    content = models.TextField(max_length=10000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return (
        f'{self.title[:30] + '...' if len(self.title) > 30 else self.title} -> {self.created_at}'
        )