from django.db import models
from  django.contrib.auth.models import User
# Create your models here.
class Meeting(models.Model):
    meetingtitle = models.CharField(max_length=255)
    meetingDate = models.DateField()
    meetingTime = models.TimeField()
    meetingLocation=models.CharField(max_length=255)
    meetingAgenda=models.CharField(max_length=255)

    def __str__(self):
        return self.meetingtitle
 
    class Meta:
        db_table='meeting'

    

class MeetingMinutes(models.Model):
    meetingid=models.ForeignKey(Meeting, on_delete=models.CASCADE)
    attendance=models.ManyToManyField(User)
    minutesText=models.TextField()

    def __str__(self):
        return self.meetingid
 
    class Meta:
        db_table='meetingminutes'

class Resource(models.Model):
    resourceName = models.CharField(max_length=255)
    resourceType = models.CharField(max_length=255)
    resourceUrl = models.URLField(null=True, blank=True)
    dateEntered = models.DateField()
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    resourceDescription=models.CharField(max_length=255)
    

    def __str__(self):
        return self.resourceName
 
    class Meta:
        db_table='resource'


class Event(models.Model):
    eventTitle = models.CharField(max_length=255)
    eventLocation = models.CharField(max_length=255)
    eventDate = models.DateField()
    eventTime = models.TimeField()
    eventDescription = models.TextField(null=True)
    resourceUrl = models.URLField(null=True, blank=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.eventTitle
 
    class Meta:
        db_table='event'