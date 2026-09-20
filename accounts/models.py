from django.db import models

# Create your models here.
from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.contrib.auth.models import Group


@receiver(post_migrate)
def create_roles(sender, **kwargs):
    for name in ('Owner', 'Staff'):
        Group.objects.get_or_create(name=name)
