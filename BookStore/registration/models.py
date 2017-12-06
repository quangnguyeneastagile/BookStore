from django.db import models
from django.utils import timezone

# Create your models here.
class User(models.Model):
    userId = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    fullName = models.CharField(max_length=200)
    birthday = models.DateField(blank=True, null=True)
    accountCreatedDate = models.DateField(default=timezone.datetime.today)

    def create(self):
        self.accountCreatedDate = timezone.timezone.datetime.today()

    def __str__(self):
        return self.userId
