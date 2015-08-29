from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'Next2U/index.html')

def agency_registration(request):
    return render(request, 'Next2U/agency.html')