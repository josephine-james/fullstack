from django.shortcuts import render
from .models import Event
from .forms import Applicantform
# Create your views here.
def index(request):
    event = Event.objects.all()
    context = {
        'events': event
    }
    return render(request, 'eventapp/index.html', context)

def detail(request, pk):
    eve_det = Event.objects.get(pk=pk)
    if request.method == 'POST':
        form = Applicantform(request.POST)
        if form.is_valid():
            applicant = form.save(commit=False)
            applicant.event = eve_det
            applicant.save()

    form = Applicantform()
    context = {
        'events': eve_det,
        'form' : form
    }
    return render(request, 'eventapp/detail.html', context)
