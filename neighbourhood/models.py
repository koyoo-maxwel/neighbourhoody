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



class Hood(models.Model):
    name = models.CharField(max_length=90)
    location = models.CharField(max_length=90)
    count = models.IntegerField()
    admin = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name

    def create_hood(self):
        self.save

    def delete_hood(self):
        self.delete

    @classmethod
    def get_hood(cls):
        hood = cls.objects.all()
        return hood