from django.db import models
from django.contrib.auth.models import User

class Friend(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner', null=True)
    friends = models.ManyToManyField(User)
    
    @classmethod
    def add_friend(cls, current_user, friend):
        user, created = cls.objects.get_or_create( # "get_or_create" method doesn`t return just the @object it self@ it`s return also the object @created or not@
            user = current_user
        )
        user.friends.add(friend)


    @classmethod
    def remove_friend(cls, current_user, friend):
        user, created = cls.objects.get_or_create(
            user = current_user
        )
        user.friends.remove(friend)