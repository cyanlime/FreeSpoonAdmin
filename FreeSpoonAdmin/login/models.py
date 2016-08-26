from __future__ import unicode_literals

from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    def __unicode__(self):
        return self.name
    