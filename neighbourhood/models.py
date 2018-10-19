from django.db import models
from tinymce.models import HTMLField
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

# Create your models here.


class GroupExtend(models.Model):
    group = models.OneToOneField(Group)

    def create_group(self):
        self.save

    def delete_group(self):
        self.delete

    def __str__(self):
        return self.group


# The neighbour
class Jirani(models.Model):
    name = models.CharField(max_length=90)
    location = models.CharField(max_length=90)
    count = models.IntegerField()
    admin = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def create_jirani(self):
        self.save

    def delete_jirani(self):
        self.delete

    @classmethod
    def get_jirani(cls):
        jirani = cls.objects.all()
        return jirani

    @classmethod
    def find_jirani(cls, jirani_id):
        query = cls.objects.filter(user__name__icontains=jirani_id)
        return query

    @classmethod
    def update_jirani(cls):
        jirani = cls.objects.all()
        return jirani

    @classmethod
    def update_count(cls):
        count = cls.objects.all()
        return count

    def __str__(self):
        return self.name


# jirani's busines
class Business(models.Model):
    name = models.CharField(max_length=90)
    jirani = models.ForeignKey(Jirani, on_delete=models.CASCADE, null=True)
    email = models.EmailField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def create_business(self):
        self.save

    def delete_business(self):
        self.delete

    @classmethod
    def get_business(self):
        business = Business.objects.all()
        return business

    @classmethod
    def searched_business(cls, search_term):
        business = cls.objects.filter(user__username__icontains=search_term)
        return business

    @classmethod
    def update_business(cls):
        update = cls.objects.all()
        return update

    def __str__(self):
        return self.name


# user profile model
class Profile(models.Model):
    name = models.CharField(max_length=90)
    image = models.ImageField(upload_to='profile_photos/', null=True, blank=True)
    id = models.IntegerField
    jirani = models.ForeignKey(Jirani, on_delete=models.CASCADE, null=True)
    email = models.EmailField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    

    def create_profile(self):
        self.save

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete

    @classmethod
    def update_profile(self):
        profile_update = cls.objects.filter(id).all()
        return profile_update

    @classmethod
    def get_profile(self):
        profile = Profile.objects.all()
        return profile

    def __str__(self):
        return str(self.image)


# my jirani posts
class Post(models.Model):
    title = models.CharField(max_length=90, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='post/', null=True, blank=True)
    caption = models.CharField(max_length=100)
    jirani = models.ForeignKey(Jirani, on_delete=models.CASCADE, null=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)

    def create_post(self):
        self.save

    def delete_post(self):
        self.delete

    @classmethod
    def get_post(cls):
        post = Post.objects.all()
        return post

    @classmethod
    def get_profile_posts(cls, profile_id):
        profile_posts = Post.objects.filter(id=profile_id)
        return profile_posts

    def __str__(self):
        return self.title
