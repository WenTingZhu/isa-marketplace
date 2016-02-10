from django.shortcuts import render
from django.http import HttpResponse
import datetime

def home(request):
    #return render(request, 'index.html')
    now = datetime.datetime.now()
    html = "<html><body>It is now sometime.</body></html>"
    return HttpResponse(html)
