from django.shortcuts import render
from django.http import HttpResponse
import datetime
from django.contrib.auth.models import User

def home(request):
    #return render(request, 'index.html')
    now = datetime.datetime.now()

    u = User.objects.create(first_name=str(now), username=str(now))
    u.save()

    html = "<html><body>{}</body></html>".format(u.first_name)

    return HttpResponse(html)
