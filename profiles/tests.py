from django.test import TestCase
from django.contrib.auth.models import User
from django.test import Client
from django.contrib import auth

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




    # def login(self):
    #     self.client.login(username='alen', password='test')

    # def test_connected_user_should_be_logged_in(self):
    #     user = self.create_user()

    #     self.assertTrue(self.client.session.get('_auth_user_id', False))

    # def tester2(self):
    #     j = 2
    #     self.assertEqual(j,2) 
class dummyTest(TestCase):
    def tester(self):
        i = 1
        self.assertEqual(i,1)
    def tester2(self):
        j = 2
        self.assertEqual(j,2) 