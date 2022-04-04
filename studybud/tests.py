from studybud.models import Session
from django.test import TestCase
from django.core.exceptions import ValidationError
import django

class PostSessionTest(TestCase):
    # To test that sessions with invalid dates don't get added to the database.
    # Expected results: Invalid session raises a validation error
    def test_invalid_date(self):
        with self.assertRaises(django.core.exceptions.ValidationError):
            k = Session(attendees=1, date="a", location="Rice Hall", details="This session is being created as a test.")
            k.save()
            self.assertEqual(k.details,"This session is being created as a test.")

    # To test that sessions with descriptions that are too long don't get added to the database.
    # Expected results: Invalid session raises a validation error
    def test_invalid_course_description(self):
        with self.assertRaises(AssertionError):
            k = Session(attendees=1, date="2022-03-26 20:40:02.541566+00:00", location="Rice Hall", details="oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo\
                oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo\
                    oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo")
            k.save()
            self.assertEqual(k.details,"This session is being created as a test.")

    # To test that valid sessions get added to the database.
    # Expected results: Valid session has an id (was added to the database)
    def test_valid_session_has_id(self):
        s = s = Session(attendees=1, date="2022-03-26 20:40:02.541566+00:00", location="Rice Hall", details="This session is being created as a test.")
        s.save()
        self.assertTrue(type(s.id) is int)

    # To test that valid sessions get added to the database.
    # Expected results: The database has 7 entries with location "test0001" when 2 sessions are posted with this location
    def test_valid_session_loads_correctly(self):
        s = Session(attendees=1, date="2022-03-26 20:40:02.541566+00:00", location="test0001", details="This session is being created as a test.")
        k = Session(attendees=1, date="2022-03-26 20:40:02.541566+00:00", location="test0001", details="This session is being created as a test.")
        a = Session(attendees=1, date="2022-03-26 20:40:02.541566+00:00", location="test0001", details="This session is being created as a test.")
        b = Session(attendees=1, date="2022-03-26 20:40:02.541566+00:00", location="test0001", details="This session is being created as a test.")
        c = Session(attendees=1, date="2022-03-26 20:40:02.541566+00:00", location="test0001", details="This session is being created as a test.")
        d = Session(attendees=1, date="2022-03-26 20:40:02.541566+00:00", location="test0001", details="This session is being created as a test.")
        e = Session(attendees=1, date="2022-03-26 20:40:02.541566+00:00", location="test0001", details="This session is being created as a test.")
        s.save()
        k.save()
        a.save()
        b.save()
        c.save()
        d.save()
        e.save()
        self.assertEqual(len(Session.objects.filter(location__startswith="test0001")), 7)

    # To test that valid sessions get added to the database.
    # Expected results: The database has an entry matching the details of the new session posted
    def test_entry_creation(self):
        s = Session(attendees=1, date="2022-03-26 20:40:02.541566+00:00", location="test0002", details="This session is being created as a test.")
        s.save()
        self.assertEqual(s.details,"This session is being created as a test.")
    
     # To test that valid sessions get added to the database.
    # Expected results: Entry matches 
    def test_entry_creation(self):
        s = Session(attendees=1, date="2022-03-26 20:40:02.541566+00:00", location="test0002", details="This session is being created as a test.")
        s.save()
        self.assertEqual(s.details,"This session is being created as a test.")
    
    