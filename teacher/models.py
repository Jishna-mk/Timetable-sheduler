from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    subject_taught1 = models.CharField(max_length=100,null=True)
    subject_taught2 = models.CharField(max_length=100,null=True)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return self.user.get_full_name() or self.user.username