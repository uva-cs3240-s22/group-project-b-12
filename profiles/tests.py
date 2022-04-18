from django.test import TestCase
from django.contrib.auth.models import User
from django.test import Client
from django.contrib import auth
from .models import Profile, Course

# class accountTest(TestCase):
#     # To check if the login page redirects users to the home page if they're not logged in
#     # Expected result: No redirect occurs
#     def test_user_not_logged_in(self):
#         response = self.client.get('/profiles', follow=True)
#         self.assertEqual(response.redirect_chain[0][0], "/profiles/")
    
#     # To check if the login redirects logged in users to the home page
#     # Expected result: The login page redirects logged in users to the home page
#     def test_user_logged_in(self):
#         c = Client()
#         User.objects.create_user(username='fred', password='secret')
#         c.login(username='fred', password='secret')
#         response = self.client.get('/profiles', follow=True)
#         self.assertTrue(response.redirect_chain[0][0], "/sessions/")

# class ProfileTest(TestCase):

#     # To check that the model fields are user, bio, classes, and courses
#     # Expected result: The model returns user and bio as it's fields
#     def test_profile_fields(self):
#        self.assertEqual([f.name for f in Profile._meta.get_fields()], ['user','bio', 'classes', 'courses'])

#     # To check that the profile model doesn't accept invalid values as users
#     # Expected result: It raises a value error when you try to put a string instead of a user
#     def test_invalid_profile_user(self):
#         with self.assertRaises(ValueError):
#             k = Profile('test','test')
#             k.save()
    
#     # To check that profiles with no bios, classes, or courses are created (null is accepted)
#     # Expected result: Profile k is successfully created with no bio
#     def test_no_profile_bio(self):
#         user = User.objects.create_user(username='testuser', password='12345')
#         k = Profile(user.id)
#         k.save()

#     # To check that profiles with no user don't get created
#     # Expected result: Profile k raises a value error because it has no user argument
#     def test_no_profile_user(self):
#         with self.assertRaises(ValueError):
#             k = Profile('bio')
#             k.save()

#     # To check that the profile model accepts valid values
#     # Expected result: The k profile is successfully created
#     def test_valid_profile_creation(self):
#         user = User.objects.create_user(username='testuser', password='12345')
#         k = Profile(user.id, 'test')
    
#     # To check that the database saves profile models with correct values
#     # Expected result: The k profile is successfully saved into the database
#     def test_valid_profile_save(self):
#         user = User.objects.create_user(username='testuser', password='12345')
#         k = Profile(user.id, 'test')
#         k.save()
    
# class CoursesTest(TestCase):

#     # To check that the course model accepts valid values
#     # Expected result: The course k is successfully created
#     def test_valid_course(self):
#         k = Course(instructor="Will McBurney", catalog_number="3240", subject="CS")

#     # To check that valid courses are succesfully saved into the database
#     # Expected result: The course k is successfuly saved into the database
#     def test_saving_valid_course(self):
#         k = Course(instructor="Will McBurney", catalog_number="3240", subject="CS")
#         k.save()
    
#     # To check that valid courses are succesfully added to user profiles
#     # Expected result: The course k is successfully saved into profile p
#     def test_adding_course_to_profile(self):
#         k = Course(instructor="Will McBurney", catalog_number="3240", subject="CS")
#         k.save()
#         user = User.objects.create_user(username='testuser', password='12345')
#         p = Profile(user.id, 'test')
#         p.save()
#         p.courses.add(k)
    
#     # To check that profiles don't accept invalid values as course
#     # Expected result: The course k rasies a value error after attemtping to add to profile p
#     def test_adding_invalid_course_value_to_profile(self):
#         with self.assertRaises(ValueError):
#             user = User.objects.create_user(username='testuser', password='12345')
#             p = Profile(user.id, 'test')
#             p.save()
#             k = "test"
#             p.courses.add(k)
    
#     # To check that multiple courses can be added to profile
#     # Expected result: Profile p returns 3 courses when 3 courses are added
#     def test_adding_multiple_courses_to_profile(self):
#         a = Course(instructor="Will McBurney", catalog_number="3240", subject="CS")
#         a.save()
#         b = Course(instructor="Mark Floryan", catalog_number="2150", subject="CS")
#         b.save()
#         c = Course(instructor="Robbie Hott", catalog_number="4640", subject="CS")
#         c.save()

#         user = User.objects.create_user(username='testuser', password='12345')
#         p = Profile(user.id, 'test')
#         p.save()
#         p.courses.add(a)
#         p.courses.add(b)
#         p.courses.add(c)

