from studybud.models import Session
from django.test import TestCase
from django.core.exceptions import ValidationError
import django
from profiles.models import Course
from django.contrib.auth.models import User

class PostSessionTest(TestCase):
    # To test that sessions with invalid dates don't get added to the database.
    # Expected results: Invalid session raises a validation error
    def test_invalid_date(self):
        with self.assertRaises(django.core.exceptions.ValidationError):
            attendee = User.objects.create_user(username='testuser', password='12345')
            attendee.save()
            a = Course(instructor="Will McBurney", catalog_number="3240", subject="CS")
            a.save()    
            k = Session(date="a", location="Rice Hall", details="This session is being created as a test.", course=a, host = attendee)
            k.save()
            self.assertEqual(k.details,"This session is being created as a test.")

    # To test that sessions with descriptions that are too long don't get added to the database.
    # Expected results: Invalid session raises a validation error
    def test_invalid_course_description(self):
        with self.assertRaises(AssertionError):
            attendee = User.objects.create_user(username='testuser', password='12345')
            attendee.save()
            a = Course(instructor="Will McBurney", catalog_number="3240", subject="CS")
            a.save()  
            k = Session(date="2022-03-26 20:40:02.541566+00:00", location="Rice Hall", details="oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo\
                oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo\
                    oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo", course=a, host= attendee)
            k.save()
            self.assertEqual(k.details,"This session is being created as a test.")

    # To test that valid sessions get added to the database.
    # Expected results: Valid session has an id (was added to the database)
    def test_valid_session_has_id(self):
        attendee = User.objects.create_user(username='testuser', password='12345')
        attendee.save()
        a = Course(instructor="Will McBurney", catalog_number="3240", subject="CS")
        a.save()  
        s = s = Session(date="2022-03-26 20:40:02.541566+00:00", location="Rice Hall", details="This session is being created as a test.", course = a, host = attendee)
        s.save()
        self.assertTrue(type(s.id) is int)

    # To test that valid sessions get added to the database.
    # Expected results: The database has 7 entries with location "test0001" when 2 sessions are posted with this location
    def test_valid_session_loads_correctly(self):
        attendee = User.objects.create_user(username='testuser', password='12345')
        attendee.save()
        a = Course(instructor="Will McBurney", catalog_number="3240", subject="CS")
        a.save()  
        s = Session(date="2022-03-26 20:40:02.541566+00:00", location="test0001", details="This session is being created as a test.", course = a, host = attendee)
        k = Session(date="2022-03-26 20:40:02.541566+00:00", location="test0001", details="This session is being created as a test.", course = a, host = attendee)
        p = Session(date="2022-03-26 20:40:02.541566+00:00", location="test0001", details="This session is being created as a test.", course = a, host = attendee)
        b = Session(date="2022-03-26 20:40:02.541566+00:00", location="test0001", details="This session is being created as a test.", course = a, host = attendee)
        c = Session(date="2022-03-26 20:40:02.541566+00:00", location="test0001", details="This session is being created as a test.", course = a, host = attendee)
        d = Session(date="2022-03-26 20:40:02.541566+00:00", location="test0001", details="This session is being created as a test.", course = a, host = attendee)
        e = Session(date="2022-03-26 20:40:02.541566+00:00", location="test0001", details="This session is being created as a test.", course = a, host = attendee)
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
        attendee = User.objects.create_user(username='testuser', password='12345')
        attendee.save()
        a = Course(instructor="Will McBurney", catalog_number="3240", subject="CS")
        a.save()  
        s = Session(date="2022-03-26 20:40:02.541566+00:00", location="test0002", details="This session is being created as a test.", course = a, host = attendee)
        s.save()
        self.assertEqual(s.details,"This session is being created as a test.")
    
     # To test that valid sessions get added to the database.
    # Expected results: Entry matches 
    def test_entry_creation(self):
        attendee = User.objects.create_user(username='testuser', password='12345')
        attendee.save()
        a = Course(instructor="Will McBurney", catalog_number="3240", subject="CS")
        a.save()  
        s = Session(date="2022-03-26 20:40:02.541566+00:00", location="test0002", details="This session is being created as a test.", course = a, host = attendee)
        s.save()
        self.assertEqual(s.details,"This session is being created as a test.")

    #To test that study sessions require a course (can't be null)
    #Expected result: Course s doesn't save successfully
    def test_course_one_to_one_relationship(self):
        with self.assertRaises(django.db.utils.IntegrityError):
            attendee = User.objects.create_user(username='testuser', password='12345')
            attendee.save()
            s = Session(date="2022-03-26 20:40:02.541566+00:00", location="test0002", details="This session is being created as a test.", host = attendee)
            s.save()
    
class AttendeeTest(TestCase):
    # To test that an attendee is successfully get added to sessions
    # Expected results: Attendee is successfully added to session s
    def test_attendee_addition(self):
        attendee = User.objects.create_user(username='testuser', password='12345')
        attendee.save()
        a = Course(instructor="Will McBurney", catalog_number="3240", subject="CS")
        a.save()  
        s = Session(date="2022-03-26 20:40:02.541566+00:00", location="Rice Hall", details="This session is being created as a test.", course = a, host = attendee)
        s.save()
        s.attendees.add(attendee)
        self.assertEqual(len(s.attendees.all()), 1)
    
    # To test that multiple attendees can be added to sessions
    # Expected results: Attendees iare successfully added to session s
    def test_multiple_attendee_addition(self):
        attendee1 = User.objects.create_user(username='testuser1', password='12345')
        attendee1.save()
        attendee2 = User.objects.create_user(username='testuser2', password='12345')
        attendee2.save()
        attendee3 = User.objects.create_user(username='testuser3', password='12345')
        attendee3.save()
        a = Course(instructor="Will McBurney", catalog_number="3240", subject="CS")
        a.save()  
        s = Session(date="2022-03-26 20:40:02.541566+00:00", location="Rice Hall", details="This session is being created as a test.", course = a, host = attendee1)
        s.save()
        s.attendees.add(attendee1, attendee2, attendee3)
        self.assertEqual(len(s.attendees.all()), 3)
    
class HostTest(TestCase):

    # Test that host accepts user as parameter
    # Expected result: Session s is successfully created
    def test_valid_host_field(self):
        attendee = User.objects.create_user(username='testuser1', password='12345')
        attendee.save()
        a = Course(instructor="Will McBurney", catalog_number="3240", subject="CS")
        a.save()  
        s = Session(date="2022-03-26 20:40:02.541566+00:00", location="Rice Hall", details="This session is being created as a test.", course = a, host = attendee)
        s.save()
        
    # Test that host is a required field (can't be null)
    # Expected result: Session s raises 
    def test_null_host_field(self):
        with self.assertRaises(django.db.utils.IntegrityError):
            a = Course(instructor="Will McBurney", catalog_number="3240", subject="CS")
            a.save()  
            s = Session(date="2022-03-26 20:40:02.541566+00:00", location="Rice Hall", details="This session is being created as a test.", course = a)
            s.save()
