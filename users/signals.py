from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import User
from django.conf import settings


def createProfile(sender, instance, created, **kwargs):
    if created:
        user = instance
        profile = User.objects.create(
            user=user,
            username=user.username,
            email=user.email,
            name=user.first_name,
        )

post_save.connect(createProfile, sender=User)
