from django.db import models
from datetime import datetime, date
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token







class News(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    author = models.CharField(max_length=40)
    image = models.ImageField(null=True, blank=True)
    publication_date = models.DateField(null=True)
    owner = models.ForeignKey('auth.User', related_name='news', on_delete=models.CASCADE)
