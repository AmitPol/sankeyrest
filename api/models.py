from django.db import models
from datetime import datetime
import django


# Create your models here.
class Emp(models.Model):
<<<<<<< HEAD
    id = models.IntegerField(auto_created=True, primary_key=True)
=======
    _id=models.CharField(max_length=100, default='none')
    id=models.IntegerField(auto_created=True,primary_key=True)
>>>>>>> 0a2e09fb8b3b33f276a060b491c4561823b8ca46
    name = models.CharField(max_length=100, default='none')
    email = models.EmailField(default='none')
    username = models.CharField(max_length=100, default='undefined')
    password = models.CharField(max_length=32, default='none')
    role = models.CharField(max_length=100, default='Employee')
    is_active = models.BooleanField(default=True)
    created_date = models.DateTimeField(default=django.utils.timezone.now)
    end_date = models.DateTimeField(default=datetime(2100, 8, 31, 1, 32, 9, 168460))

    def __str__(self):
        return self.name
