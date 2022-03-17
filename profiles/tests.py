from django.test import TestCase

# Create your tests here.
class dummyTest(TestCase):
    def tester(self):
        i = 1
        self.assertEqual(i,1)