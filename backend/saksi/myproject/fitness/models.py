from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser,Group,Permission;

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=20,default="user")
    password = models.CharField(max_length=20)
    is_trainer = models.BooleanField(default=False)
    username = models.CharField(
        max_length=150,
        unique=True,  # Unique constraint to ensure usernames are unique
        blank=True,   # Allow empty usernames
    )
    groups = models.ManyToManyField(Group, related_name="custom_users")
    user_permissions = models.ManyToManyField(Permission, related_name="custom_users")

