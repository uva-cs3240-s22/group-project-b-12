from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from studybud.models import Session
from django.utils import timezone
from django.views import generic
from django.urls import reverse

from django.test import TestCase 

class SessionTestCase(TestCase): 
    def setup(self): 
        Session.objects.create(attendees = 1, date='2022-03-12 07:30', location='Alderman', course='CS 3240', details = 'testing')
    def test_fields(self):
        test1 = Session.objects.get(course='CS 3240')
        self.assertEqual(Session.__str__(test1),"Study session with 1 at Alderman on March 12, 2022, 7:30 p.m. for CS 3240. Here are any additional details: testing.")


