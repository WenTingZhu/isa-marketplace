from django.shortcuts import render
from django.http import HttpResponse
import datetime
from django.contrib.auth.models import User

def home(request):
    #return render(request, 'index.html')
    now = datetime.datetime.now()

    u = User.objects.create(first_name=str(now), username=str(now))
    u.save()

    html = "<html><body>CURRENT: {}".format(u.first_name)
    html = html + "<table style=\"width:100%\">"


    for old in User.objects.all():
        html = html + "<tr><td>" +str(old.username) + "</td></tr>"
    html = html + "</table></body></html>"

    return HttpResponse(html)
