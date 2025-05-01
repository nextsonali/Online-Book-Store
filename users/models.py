import uuid
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_user(self, username, password=None):
        if not username:
            raise ValueError("Users must have a username")
        user = self.model(username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password):
        user = self.create_user(username=username, password=password)
        user.is_admin = True
        user.save(using=self._db)
        return user

class CustomUser(AbstractBaseUser):
    user_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=128)  # Password is managed by AbstractBaseUser

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username

    @property
    def is_staff(self):
        return self.is_admin
