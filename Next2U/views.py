from django.http import HttpResponse
from django.shortcuts import render
from Next2U.models import Supporter

from Next2U.models import Agency
import sqlite3

# Create your views here.
def index(request):
   return render(request, 'Next2U/index.html')

def agencyRegistrationDisplay(request):
    return render(request, 'Next2U/agency.html')

def mentorRegistrationDisplay(request):
    return render(request, 'Next2U/mentor.html')

def agencyRegistrationPost(request):
    agencySaved=Agency(
    Name = request.POST.get("Name"),
    ContactName = request.POST.get("ContactName"),
    TINNumber = request.POST.get("TINNumber"),
    Address1 = request.POST.get("Address1"),
    Address2 = request.POST.get("Address2"),
    City = request.POST.get("City"),
    State = request.POST.get("State"),
    ZIP = request.POST.get("ZIP"),
    Phone = request.POST.get("Phone"),
    Email = request.POST.get("Email"))

    agencySaved.save()
    return render(request, 'Next2U/agency.html')

def agency_search(request):
        # get the blog posts that are published
        supporters = Supporter.objects.filter()
        # now return the rendered template
        return render(request, 'Next2U/agencysearch.html')

