from django.contrib.auth.models import User
from django.db import models

def generate_user_avatar_path(instance, filename):
    return f"users/user_{instance.user.pk}/avatar/{filename}"


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    agreement_accepted = models.BooleanField(default=False)
    avatar = models.ImageField(null=True, blank=True, upload_to=generate_user_avatar_path)
    
    
