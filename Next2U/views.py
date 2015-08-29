from django.shortcuts import render
import sqlite3

# Create your views here.
def index(request):
    return render(request, 'Next2U/index.html')

def agency_registration(request):
    return render(request, 'Next2U/agency.html')

def mentor_registration(request):
    return render(request, 'Next2U/mentor.html')

def agencypost(request):
    #import ipdb
    #ipdb.set_trace()
    #conn = sqlite3.connect('db.sqlite3')
    #c=conn.cursor()
    #c.execute("INSERT INTO Next2U_agency VALUES (1, 'Nitu','Shukla','testing','Address1','Address2','city','state','zip','phone','email')")
    #conn.commit()
    #conn.close()
    return render(request, 'Next2U/index.html')