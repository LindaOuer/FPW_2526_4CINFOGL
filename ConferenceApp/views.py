from django.shortcuts import render
from django.http import HttpResponse

from .forms import ConferenceForm
from .models import Conference
from django.views.generic import ListView, DetailView, DeleteView, CreateView
from django.urls import reverse_lazy

# Create your views here.
def home(request):
    return HttpResponse("<h1>Welcome to the Conference App Home Page!</h1>")
# page HTML => templates
# json response => API

def about(request):
    name = "Conference App"
    return render(request, 'Conference/about.html', {'app_name': name})
# context => dictionary ==> key : HTML variable name , value : variable to display

def profile(request, username):
    return render(request, 
                  'Conference/profile.html', 
                  {'username': username})
    
# username => dynamic part of the URL

def conferenceList(request):
    list = Conference.objects.all().order_by('-start_date') # SELECT * FROM Conference ORDER BY start_date DESC
    return render(request, 
                  'Conference/conference_list.html', 
                  {'conferences': list})
    
class ConferenceListView(ListView):
    model = Conference
    context_object_name = 'conferences'
    template_name = 'Conference/conference_list.html'
    
class ConferenceDetailView(DetailView):
    model = Conference
    context_object_name = 'conference'
    template_name = 'Conference/conference_detail.html'
    
class ConferenceDeleteView(DeleteView):
    model = Conference
    context_object_name = 'conf'
    template_name = 'Conference/conference_confirm_delete.html'
    success_url = reverse_lazy('conference_list_lv')
    
class ConferenceCreateView(CreateView):
    model = Conference
    form_class = ConferenceForm
    template_name = 'Conference/conference_form.html'
    success_url = reverse_lazy('conference_list_lv')