from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
# import requests
import json
from django.views.decorators.http import require_http_methods
from django.views.decorators.debug import sensitive_post_parameters
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.cache import never_cache
from django.contrib.auth.decorators import login_required
import frontend.status_codes
import requests
from django.conf import settings

experience = "http://" + settings.EXPERIENCE + "/"

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
    rides = []
    url = experience + "get_ride/1/"
    response = requests.get(url)
    if reponse["status"] == "200":
        rides.append(response)
    url = expereince + "get_ride/2/"
    response = requests.get(url)
    if reponse["status"] == "200":
        rides.append(response)
    return render(request, "dashboard.html", {'user': user, "rides": rides, "authenticated": True})

def rides(request):
    # invalid_login = request.session.pop('invalid_login', False)

    # if request.user.is_authenticated():
    #     return redirect('dashboard')
    rides = [
    {'driver': 'driverid1', 'available_seats': 3, 'from': 'nova', 'to':'uva', 'departure_time':'today'},
    {'driver': 'driverid2', 'available_seats': 4, 'from': 'nova1', 'to':'uva1', 'departure_time':'today'},
    {'driver': 'driverid1', 'available_seats': 3, 'from': 'nova', 'to':'uva', 'departure_time':'today'},
    {'driver': 'driverid2', 'available_seats': 4, 'from': 'nova1', 'to':'uva1', 'departure_time':'today'},
    {'driver': 'driverid1', 'available_seats': 3, 'from': 'nova', 'to':'uva', 'departure_time':'today'},
    {'driver': 'driverid2', 'available_seats': 4, 'from': 'nova1', 'to':'uva1', 'departure_time':'today'},
    {'driver': 'driverid1', 'available_seats': 3, 'from': 'nova', 'to':'uva', 'departure_time':'today'},
    {'driver': 'driverid2', 'available_seats': 4, 'from': 'nova1', 'to':'uva1', 'departure_time':'today'},
    {'driver': 'driverid1', 'available_seats': 3, 'from': 'nova', 'to':'uva', 'departure_time':'today'},
    {'driver': 'driverid2', 'available_seats': 4, 'from': 'nova1', 'to':'uva1', 'departure_time':'today'},
    {'driver': 'driverid1', 'available_seats': 3, 'from': 'nova', 'to':'uva', 'departure_time':'today'},
    {'driver': 'driverid2', 'available_seats': 4, 'from': 'nova1', 'to':'uva1', 'departure_time':'today'},
    {'driver': 'driverid2', 'available_seats': 4, 'from': 'nova1', 'to':'uva1', 'departure_time':'today'},
    {'driver': 'driverid1', 'available_seats': 3, 'from': 'nova', 'to':'uva', 'departure_time':'today'},
    {'driver': 'driverid2', 'available_seats': 4, 'from': 'nova1', 'to':'uva1', 'departure_time':'today'},
    {'driver': 'driverid1', 'available_seats': 3, 'from': 'nova', 'to':'uva', 'departure_time':'today'},
    {'driver': 'driverid2', 'available_seats': 4, 'from': 'nova1', 'to':'uva1', 'departure_time':'today'},
    {'driver': 'driverid1', 'available_seats': 3, 'from': 'nova', 'to':'uva', 'departure_time':'today'},
    {'driver': 'driverid2', 'available_seats': 4, 'from': 'nova1', 'to':'uva1', 'departure_time':'today'},
    {'driver': 'driverid1', 'available_seats': 3, 'from': 'nova', 'to':'uva', 'departure_time':'today'},
    ]
    user = "John Doe"
    return render(request, "rides.html", {"user":user, "authenticated":True, "rides": rides})
