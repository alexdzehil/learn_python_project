from django.db import models
from django.contrib.auth.models import User


class Profiles(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    bio = models.CharField(max_length=200, null=True)
    profile_pic = models.ImageField(default='profile_default.png', null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    following = models.ManyToManyField(User, related_name='following', blank=True)

    def __str__(self):
        return str(self.user.username)
