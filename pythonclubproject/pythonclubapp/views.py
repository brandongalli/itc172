from django.shortcuts import render, get_object_or_404
from .models import Meeting, MeetingMinutes, Resource, Event
from .forms import ProductForm, ResourceForm
from django.contrib.auth.decorators import login_required

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

@login_required
def newProduct(request):
    form = ProductForm
    if request.method=='POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            post = form.save(commit=True)
            post.save()
            form=ProductForm()
    else:
        form=ProductForm()

    return render(request, 'pythonclubapp/newclub.html', context={'form': form})

@login_required
def newResource(request):
    form = ResourceForm
    if request.method=='POST':
        form = ResourceForm(request.POST)
        if form.is_valid():
            post = form.save(commit=True)
            post.save()
            form=ResourceForm()
    else:
        form=ResourceForm()

    return render(request, 'pythonclubapp/newresource.html', context={'form': form})

def loginMessage(request):
    return render(request, 'pythonclubapp/loginmessage.html')

def logoutMessage(request):
    return render(request, 'pythonclubapp/logoutmessage.html')
