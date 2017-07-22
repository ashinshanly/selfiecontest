from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title



class UserProfile(models.Model):
    """docstring for ClassName"""
    user = models.OneToOneField(User)
    email = models.CharField(max_length=100, default='')
    city = models.CharField(max_length=100, default='')
    college = models.CharField(max_length=100, default='')
    phone = models.IntegerField(default=0)
    

def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user = kwargs['instance'])


post_save.connect(create_profile, sender=User)
