from django.test import TestCase
from .models import Neighbourhood,Business,User,Post,Comments
from django.contrib.auth.models import User


# Create your tests here.
class NeighborhoodTestClass(TestCase):
    def setUp(self):
        self.new_user = User(username='koyoo',email='koyoomaxwel@gmail.com')
        self.new_user.save()
        self.kobel = Neighbourhood(name='Kobel',location='kobel',occupants=5)
        self.kobel.save()

    def tearDown(self):
        User.objects.all().delete()
        Neighbourhood.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.kobel,Neighbourhood))

    def test_save_neighborhood(self):
        self.kobel.save_neighborhood()
        neighborhood = Neighbourhood.objects.all()
        self.assertTrue(len(neighborhood)>0)




class BusinessTestClass(TestCase):
    def setUp(self):
        self.new_user=User(username="koyoo",email="koyoomaxwel@gmail.com")
        self.new_user.save()
        self.kobel = Neighbourhood(name='Kobel',location='kobel',occupants_count=5,admin=self.new_user)
        self.kobel.save_neighborhood()
        self.kinyozi = Business(name='Butchery',email='koyoomaxwel@gmail.com',user=self.new_user,neighborhood=self.kobel)
        self.Butchery.save()

    def tearDown(self):
        User.objects.all().delete()
        Neighbourhood.objects.all().delete()
        Business.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.Butchery,Business))

    def test_save_business(self):
        self.Butchery.save_business()
        business =  Business.objects.all()
        self.assertTrue(len(business)>0)




class PostTestClass(TestCase):
    def setUp(self):
        self.new_user=User(username="koyoo",email="koyoomaxwel@gmail.com")
        self.new_user.save()
        self.kobel = Neighbourhood(name='kobel',location='kiboswa',occupants_count=5,admin=self.new_user)
        self.kobel.save_neighborhood()
        self.koyoo = User(name="koyoo",user=self.new_user,neighborhood=self.kobel)
        self.koyoo.save_user()
        self.new_post=Post(post='Plumber in the hood',author=self.koyoo)

    def tearDown(self):
        User.objects.all().delete()
        Neighbourhood.objects.all().delete()
        User.objects.all().delete()
        Post.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_post,Post))

    def test_save_post(self):
        self.new_post.save_post()
        post =  Post.objects.all()
        self.assertTrue(len(post)>0)




class UserTestClass(TestCase):
    def setUp(self):
        self.new_user=User(username="koyoo",email="koyoomaxwel.com")
        self.new_user.save()
        self.kobel = Neighbourhood(name='Kobel',location='Kiboswa',occupants_count=5,admin=self.new_user)
        self.kobel.save_neighborhood()
        self.koyoo = User(name="maxwell",user=self.new_user,neighborhood=self.kobel)
        self.koyoo.save()

    def tearDown(self):
        User.objects.all().delete()
        Neighbourhood.objects.all().delete()
        User.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.koyoo,User))
