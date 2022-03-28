from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.db import models
from studybud.models import Session
from django.utils import timezone
from django.views import generic
from django.urls import reverse

from django.test import TestCase 

class SessionTestCase(TestCase): 
    def setup(self): 
        #Testing the creation of a session
        session = Session.objects.create(date='2022-03-12 07:30', location='Alderman', course='CS 3240', details = 'testing')
    
    def test_fields(self):
        #Testing the input fields of the session created
        session = Session.objects.create(date='2022-03-12 07:30', location='Alderman', course='CS 3240', details = 'testing')
        #test1 = Session.objects.get(course='CS 3240')
        return self.assertEqual(Session.__str__(session),"Study session at Alderman on 2022-03-12 07:30 for CS 3240. Here are any additional details: testing.")
