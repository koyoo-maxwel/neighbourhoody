from django.db import models
from tinymce.models import HTMLField
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

# Create your models here.

class GroupExtend(models.Model):
    group = models.OneToOneField(Group)

    def __str__(self):
        return self.group

    def create_group(self):
        self.save

    def delete_group(self):
        self.delete
