from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Image 

    def __str__(self):
        return (self.user.username)

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    timestamp = models.DateTimeField(default = timezone.now)
    content = models.TextField(blank=True)

    class Meta:
        ordering = ['-timestamp']
    
    def __str__(self):
        return f'{self.user.username}: {self.content}'