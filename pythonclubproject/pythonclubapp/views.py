from django.shortcuts import render, get_object_or_404
from .models import Meeting, MeetingMinutes, Resource, Event

# Create your views here.
def index(request):
    return render(request, 'pythonclubapp/index.html')

def getResources(request):
    resources_list = Resource.objects.all()
    context={'resources_list' : resources_list }
    return render(request, 'pythonclubapp/resources.html', context=context)

def getMeetings(request):
    meeting_list = Meeting.objects.all()
    return render(request, 'pythonclubapp/meetings.html', context= {'meeting_list': meeting_list})

def meetingsDetail(request, id):
    meeting = get_object_or_404(Meeting, pk=id)
    meetingcount = Meeting.objects.filter(pk=id).count()
    context = {'meeting': meeting, 'count': meetingcount}
    return render(request, 'pythonclubapp/meetingsdetail.html', context=context)
