from django.http import HttpResponse, HttpResponsePermanentRedirect
from django.shortcuts import render, render_to_response

from Next2U.models import Agency, Supporter, SupporterService, Service, AgencySupporterApproval

import sqlite3

# Create your views here.
def index(request):
   return render(request, 'Next2U/index.html')

def agencyRegistrationDisplay(request):
    return render(request, 'Next2U/agency.html')

def mentorRegistrationDisplay(request):
    return render(request, 'Next2U/mentor.html')

def mentorSuccessDisplay(request):
    return render(request, 'Next2U/mentorSuccess.html')

def signinDisplay(request):
    return render(request, 'Next2U/signin.html')

def mentorCreationDisplay(request):
    supporter = request.GET.get('id')
    return render(request, 'Next2U/mentorCreation.html', {
        'supporter': supporter
    })


def agencyRegistrationPost(request):
    agencySaved=Agency(
        Username = request.POST.get("username"),
        Password = request.POST.get("password"),
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
    supporters = Supporter.objects.all()
    agencyid = agencySaved.id
    # now return the rendered template    
    return render(request, 'Next2U/agencysearch.html', {'supporters':supporters, 'Agency':agencyid})


def mentorRegistrationPost(request):
    mentorSaved=Supporter(
        Username = request.POST.get("username"),
        Password = request.POST.get("password"),
        FirstName = request.POST.get("FirstName"),
        LastName = request.POST.get("LastName"),
        Address1 = request.POST.get("Address1"),
        Address2 = request.POST.get("Address2"),
        City = request.POST.get("City"),
        State = request.POST.get("State"),
        ZIP = request.POST.get("ZIP"),
        Phone = request.POST.get("Phone"),
        Email = request.POST.get("Email"))

    mentorSaved.save()
    return render(request, 'Next2U/mentorSuccess.html', {
        'Supporter': mentorSaved.id
    })

def agencySearch(request):
        import ipdb
        ipdb.set_trace()

        # get the blog posts that are published
        supporters = Supporter.objects.all().select_related
        agencyid = 1
        # now return the rendered template
        return render(request, 'Next2U/agencysearch.html', {'supporters':supporters, 'Agency':agencyid})


def loginPost(request):
    if (request.POST.get("type") == "agency"):
        #agency = Agency.objects.filter(Username=request.GET.get("username") ).filter(Password = request.GET.get("password"))
        #if (agency is None)
        #alert
        return HttpResponsePermanentRedirect("/agencySearch")
    else:
        supporter = Supporter.objects.filter(Username=request.POST.get("username") ).filter(Password = request.POST.get("password"))
        return render(request, 'Next2U/mentorCreation.html')

def saveService(request):
    supporter = Supporter.objects.get(id=request.POST.get('Supporter'))
    service = Service.objects.get(ServiceName=request.POST.get('Service'))

    supporterServiceSaved=SupporterService(
        Service = service,
        Supporter = supporter)

    supporterServiceSaved.save()
    return render(request, 'Next2U/selectionSuccess.html')

def postView(request):
    agencyid=request.GET.get('Agency')
    mentorSupportSaved=AgencySupporterApproval(
        Agency = Agency.objects.get(id=agencyid),
        Supporter = Supporter.objects.get(id=request.GET.get('supporterid'))
    )
    if (request.GET.get('checkflag')):
        mentorSupportSaved.save()

    supporters = Supporter.objects.all().select_related
    return render(request, 'Next2U/agencysearch.html', {'supporters':supporters, 'Agency':agencyid})
