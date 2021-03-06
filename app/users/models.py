from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    email = models.EmailField(blank=True, null=True)
    is_student = models.BooleanField()
    is_teacher = models.BooleanField()

    def __str__(self):
        return self.username


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
