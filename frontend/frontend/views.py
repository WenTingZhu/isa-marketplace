from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
# import requests
import json
from django.views.decorators.http import require_http_methods
from django.views.decorators.debug import sensitive_post_parameters
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.cache import never_cache
from django.contrib.auth.decorators import login_required
from frontend.status_codes import *
import requests
from django.conf import settings

experience = "http://" + settings.EXPERIENCE + ":8000/"

def index(request):
    invalid_login = request.session.pop('invalid_login', False)

    if request.user.is_authenticated():
        return redirect('dashboard')

    return render(request, "index.html", {"invalid_login": invalid_login, "authenticated": False})

@sensitive_post_parameters()
@csrf_protect
@never_cache
@require_http_methods(["POST"])
def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        data = {'username': username, 'password': password}
        url = experience + "autheticate_user/"
        # Send request to experience and get response
        # response = requests.post(url, data=json.dumps(data).encode('utf8'), headers={'content-type': 'application/json'})
        response = 202
        if response == 202:
            return redirect('dashboard')
        else:
            request.session['invalid_login'] = True
            return redirect('index')
    return redirect('index')

# @login_required(login_url='/login')
def dashboard(request):
    # Grab user data
    user = "John Doe"
    rides = []
    url = experience + "get_ride/1/"
    response = requests.get(url)
    if response.status_code == HTTP_200_OK:
        rides.append(response)
    # url = expereince + "get_ride/2/"
    # response = requests.get(url)
    # if reponse["status"] == "200":
    #     rides.append(response)
    return render(request, "dashboard.html", {'user': user, "rides": rides, "authenticated": True})

def rides(request):
    # invalid_login = request.session.pop('invalid_login', False)

    # if request.user.is_authenticated():
    #     return redirect('dashboard')
    driver_rides = [
    {'date': 'Mar. 2 5PM', 'dropoff_number': 2, 'passenger_number': 3, 'available_seats': 2},
    {'date': 'Mar. 5 5PM', 'dropoff_number': 1, 'passenger_number': 1, 'available_seats': 4},
    ]
    passenger_rides = [
    {'driver': 'Jane Doe', 'date': 'Mar. 3 8PM', 'passenger_number': 3, 'dropoff_number': 2},
    {'driver': 'Jane Doe', 'date': 'Mar. 12 3PM', 'passenger_number': 1, 'dropoff_number': 2},
    ]
    user = "John Doe"
    return render(request, "rides.html", {"user":user, "authenticated":True, "driver_rides": driver_rides, "passenger_rides": passenger_rides})
