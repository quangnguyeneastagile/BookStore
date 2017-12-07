from django.db import models
from django.utils import timezone
from django.conf import settings
import django.utils.safestring as safestring
# Create your models here.

class User(models.Model):
    user_id = models.CharField(max_length=200, help_text = "Enter user ID")
    email = models.CharField(max_length=200, help_text = "Enter email")
    password = models.CharField(max_length=200, help_text = "Enter password")
    phone = models.CharField(max_length=200, help_text = "Enter phone number")
    full_name = models.CharField(max_length=200, help_text = "Enter full name")
    birthday = models.DateField(blank=True, null=True, help_text = "Enter birthday")
    account_created_date = models.DateField(default=timezone.datetime.today)
    def create(self):
        self.account_created_date = timezone.timezone.datetime.today()
    def __str__(self):
        return self.user_id

class Category(models.Model):
    name = models.CharField(max_length=200, help_text = "Enter a book category")
    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=200, help_text = "Enter a book author")
    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200, help_text = "Enter book title")
    category = models.ForeignKey('Category',on_delete=models.SET_NULL, null=True)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    description = models.TextField(default="No description availalbe.")
    image = models.ImageField(upload_to='uploads/%Y/%m/%d/')

    def image_tag(self):
        if self.image:
            return safestring.mark_safe('<img src="%s%s" width="150" height="150" />' % (settings.MEDIA_URL, self.image))
        else:
            return ""
    image_tag.short_description = 'Image'
    image_tag.allow_tags = True

    def __str__(self):
        return self.title
