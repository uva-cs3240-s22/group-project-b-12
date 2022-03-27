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
        session = Session.objects.create(date='2022-03-12 07:30', location='Alderman', course='CS 3240', details = 'testing')
    #def test_fields(self):
     #   test1 = Session.objects.get(course='CS 3240')
      #  self.assertEqual(Session.__str__(test1),"Study session at Alderman on March 12, 2022, 7:30 p.m. for CS 3240. Here are any additional details: testing.")
