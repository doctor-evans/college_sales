from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.CharField(max_length=50)
    level = models.CharField(max_length=10)
    email = models.EmailField(default='user@gmail.com')
    phone_no = models.CharField(max_length=11, null = True)
    whatsapp_no = models.CharField(max_length=11,null = True)
    facebook_link = models.URLField(null = True)
    intagram_link = models.URLField(null = True)
    twitter_link = models.URLField(null = True)
    bio = models.TextField()
    profile_picture = models.ImageField(upload_to='profile/', null=True, blank = True)

    def __str__(self):
        return self.user.username



def profile_create(sender, instance, created, *args, **kwargs):
    if created:
        Profile.objects.get_or_create(user = instance)

post_save.connect(profile_create, sender = settings.AUTH_USER_MODEL)
