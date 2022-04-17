from studybud.models import Session
from django.test import TestCase
from django.core.exceptions import ValidationError
import django
from profiles.models import Course

class PostSessionTest(TestCase):
    # To test that sessions with invalid dates don't get added to the database.
    # Expected results: Invalid session raises a validation error
    def test_invalid_date(self):
        with self.assertRaises(django.core.exceptions.ValidationError):
            a = Course(instructor="Will McBurney", catalog_number="3240", subject="CS")
            a.save()    
            k = Session(attendees=1, date="a", location="Rice Hall", details="This session is being created as a test.", course=a)
            k.save()
            self.assertEqual(k.details,"This session is being created as a test.")

    # To test that sessions with descriptions that are too long don't get added to the database.
    # Expected results: Invalid session raises a validation error
    def test_invalid_course_description(self):
        with self.assertRaises(AssertionError):
            a = Course(instructor="Will McBurney", catalog_number="3240", subject="CS")
            a.save()  
            k = Session(attendees=1, date="2022-03-26 20:40:02.541566+00:00", location="Rice Hall", details="oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo\
                oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo\
                    oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo", course=a)
            k.save()
            self.assertEqual(k.details,"This session is being created as a test.")

    # To test that valid sessions get added to the database.
    # Expected results: Valid session has an id (was added to the database)
    def test_valid_session_has_id(self):
        a = Course(instructor="Will McBurney", catalog_number="3240", subject="CS")
        a.save()  
        s = s = Session(attendees=1, date="2022-03-26 20:40:02.541566+00:00", location="Rice Hall", details="This session is being created as a test.", course = a)
        s.save()
        self.assertTrue(type(s.id) is int)

    # To test that valid sessions get added to the database.
    # Expected results: The database has 7 entries with location "test0001" when 2 sessions are posted with this location
    def test_valid_session_loads_correctly(self):
        a = Course(instructor="Will McBurney", catalog_number="3240", subject="CS")
        a.save()  
        s = Session(attendees=1, date="2022-03-26 20:40:02.541566+00:00", location="test0001", details="This session is being created as a test.", course = a)
        k = Session(attendees=1, date="2022-03-26 20:40:02.541566+00:00", location="test0001", details="This session is being created as a test.", course = a)
        p = Session(attendees=1, date="2022-03-26 20:40:02.541566+00:00", location="test0001", details="This session is being created as a test.", course = a)
        b = Session(attendees=1, date="2022-03-26 20:40:02.541566+00:00", location="test0001", details="This session is being created as a test.", course = a)
        c = Session(attendees=1, date="2022-03-26 20:40:02.541566+00:00", location="test0001", details="This session is being created as a test.", course = a)
        d = Session(attendees=1, date="2022-03-26 20:40:02.541566+00:00", location="test0001", details="This session is being created as a test.", course = a)
        e = Session(attendees=1, date="2022-03-26 20:40:02.541566+00:00", location="test0001", details="This session is being created as a test.", course = a)
        s.save()
        k.save()
        p.save()
        b.save()
        c.save()
        d.save()
        e.save()
        self.assertEqual(len(Session.objects.filter(location__startswith="test0001")), 7)

    # To test that valid sessions get added to the database.
    # Expected results: The database has an entry matching the details of the new session posted
    def test_entry_creation(self):
        a = Course(instructor="Will McBurney", catalog_number="3240", subject="CS")
        a.save()  
        s = Session(attendees=1, date="2022-03-26 20:40:02.541566+00:00", location="test0002", details="This session is being created as a test.", course = a)
        s.save()
        self.assertEqual(s.details,"This session is being created as a test.")
    
     # To test that valid sessions get added to the database.
    # Expected results: Entry matches 
    def test_entry_creation(self):
        a = Course(instructor="Will McBurney", catalog_number="3240", subject="CS")
        a.save()  
        s = Session(attendees=1, date="2022-03-26 20:40:02.541566+00:00", location="test0002", details="This session is being created as a test.", course = a)
        s.save()
        self.assertEqual(s.details,"This session is being created as a test.")
        
    # To test that study sessions require a course (can't be null)
    # Expected result: Course s doesn't save successfully
    def test_course_one_to_one_relationship(self):
        with self.assertRaises(django.db.utils.IntegrityError):
            s = Session(attendees=1, date="2022-03-26 20:40:02.541566+00:00", location="test0002", details="This session is being created as a test.")
            s.save()
    