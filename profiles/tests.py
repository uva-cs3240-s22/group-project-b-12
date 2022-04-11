from django.test import TestCase
from django.contrib.auth.models import User
from django.test import Client
from django.contrib import auth
from .models import Profile
# Create your tests here.
class accountTest(TestCase):
    # To check if the login page redirects users to the home page if they're not logged in
    # Expected result: No redirect occurs
    def test_user_not_logged_in(self):
        response = self.client.get('/profiles', follow=True)
        self.assertEqual(response.redirect_chain[0][0], "/profiles/")
    
    # To check if the login redirects logged in users to the home page
    # Expected result: The login page redirects loggin users to the home page
    def test_user_logged_in(self):
        # User.objects.create_user(username='Paul McBurney', password='pass')
        # self.client.login(username='Paul McBurney', password='pass')
        # response = self.client.get('/profiles', follow=True)
        # self.assertEqual(response.redirect_chain[0][0], "/sessions/")
        # user = auth.get_user(self.client)
        # assert user.is_authenticated
        c = Client()
        User.objects.create_user(username='fred', password='secret')
        c.login(username='fred', password='secret')
        response = self.client.get('/profiles', follow=True)
        self.assertTrue(response.redirect_chain[0][0], "/sessions/")
        # user = User.objects.create_user(username='Paul McBurney', password='pass')
        # user.save()
        # self.client.login(username='alen', password='test')

class ProfileTest(TestCase):

    # To check that the model fields are only user and bio
    # Expected result: The model returns user and bio as it's fields
    def test_profile_fields(self):
       self.assertEqual([f.name for f in Profile._meta.get_fields()], ['user','bio'])

    # To check that the profile model doesn't accept invalid values as users
    # Expected result: It raises a value error when you try to put a string instead of a user
    def test_invalid_profile_user(self):
        with self.assertRaises(ValueError):
            k = Profile('test','test')
            k.save()
    
    # To check that profiles with no bios are created (null is accepted)
    # Expected result: Profile k is successfully created with no bio
    def test_no_profile_bio(self):
        user = User.objects.create_user(username='testuser', password='12345')
        k = Profile(user.id)
        k.save()

    # To check that profiles with no user don't get created
    # Expected result: Profile k raises a value error because it has no user argument
    def test_no_profile_user(self):
        with self.assertRaises(ValueError):
            k = Profile('bio')
            k.save()

    # To check that the profile model accepts valid values
    # Expected result: The k profile is successfully created
    def test_valid_profile_creation(self):
        user = User.objects.create_user(username='testuser', password='12345')
        k = Profile(user.id, 'test')
    
    # To check that the database saves profile models with correct values
    # Expected result: The k profile is successfully saved into the database
    def test_valid_profile_save(self):
        user = User.objects.create_user(username='testuser', password='12345')
        k = Profile(user.id, 'test')
        k.save()

    # def login(self):
    #     self.client.login(username='alen', password='test')
    
    # def test_connected_user_should_be_logged_in(self):
    #     user = self.create_user()
        
    #     self.assertTrue(self.client.session.get('_auth_user_id', False))
    
    # def tester2(self):
    #     j = 2
    #     self.assertEqual(j,2)