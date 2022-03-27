from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from studybud.models import Session
from django.utils import timezone
from django.views import generic
from django.urls import reverse

from django.test import TestCase 

class SessionTestCase(TestCase): 
    def test_fields(self):
        Session.objects.create(attendees=4, date='2/4/2022', location='Alderman', course='CS 3240', details = 'testing')
        self.assertEqual(Session.__str__(),"Study session with 4 at Alderman on 2022-04-02 00:00 for CS 3240. Here are any additional details: testing.")


