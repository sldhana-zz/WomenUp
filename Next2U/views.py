from django.shortcuts import render
import sqlite3

# Create your views here.
def index(request):
    return render(request, 'Next2U/index.html')

def agencypost(request):
    conn = sqlite3.connect('django.db')
    c=conn.cursor()
    c.execute("INSERT INTO Agency VALUES ('Nitu','Shukla','testing','Address1','Address2','city','state','zip','phone','email')")
    conn.commit()
    conn.close()
    return render(request, 'Next2U/index.html')