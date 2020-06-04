from django.test import TestCase
from .models import Meeting, MeetingMinutes, Resource, Event
class PythonMeetingTest(TestCase):
    def test_string(self):
        type= Meeting(meetingtitle='meeting1')
        self.assertEqual(str(type), type.meetingtitle)

    def test_table(self):
        self.assertEqual(str(Meeting._meta.db_table), 'meeting')

class MeetingMinutesTest(TestCase):
    def setUp(self):
        self.type = MeetingMinutes('test')
        self.minutes = Meeting(meetingtitle='minutesText', meetingAgenda=self.type, meetingTime=800.00)

    def test_string(self):
        self.assertEqual(str(self.minutes), self.minutes.meetingtitle)

    def test_type(self):
        self.assertEqual(str(self.minutes.meetingtitle), 'minutesText')
