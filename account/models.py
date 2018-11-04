from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=300, blank=True)
    city = models.CharField(max_length=30)
    phone = models.IntegerField()
    website = models.URLField(blank=True)
    image = models.ImageField(upload_to='profile_image', blank=True)

    def __str__(self):
        return self.username.username