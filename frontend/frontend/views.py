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
from .forms import *

experience = "http://" + settings.EXPERIENCE + ":8000/"

def index(request):
    """

    """
    invalid_login = request.session.pop('invalid_login', False)

    if request.user.is_authenticated():
        return redirect('dashboard')

    signup_form = SignupForm()

    return render(request, "index.html", {"invalid_login": invalid_login, "authenticated": False, "signup_form":signup_form})

@sensitive_post_parameters()
@csrf_protect
@never_cache
@require_http_methods(["POST"])
def create_user(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return redirect('dashboard')

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
    context = {'user': user, "authenticated": True}
    url = experience + "get_ride/1/"
    response = requests.get(url)
    if response.status_code == HTTP_200_OK:
        context["data"] = str(response.json())
    else:
        context["data"] = "FAILED"
    # url = expereince + "get_ride/2/"
    # response = requests.get(url)
    # if reponse["status"] == "200":
    #     rides.append(response
    return render(request, "dashboard.html", context)

def ride_detail(request, id):
    user = "John Doe"
    context = {'user': user, "authenticated": True}
    url = experience + "get_ride/" + id + "/"
    response = requests.get(url)
    if response.status_code == HTTP_200_OK:
        data = response.json()
        data = data["data"]
        context["details"] = data
        context["data"] = data
    else:
        context["data"] = "FAILED"
    return render(request, "ride-details.html", context)

def rides(request):
    # invalid_login = request.session.pop('invalid_login', False)

    # if request.user.is_authenticated():
    #     return redirect('dashboard')
    user = "John Doe"
    authenticated = True
    # ontext = {"user":user, "authenticated":True, "driver_rides": [], "passenger_rides": []]}
    url = experience + "user_rides/1/"
    response = requests.get(url)
    if response.status_code == HTTP_200_OK:
        data = response.json()
        data = data["data"]
        driver_rides = json.loads(data["driver_rides"])
        passenger_rides = json.loads(data["passenger_rides"])

        return render(request, "rides.html", {'user': user, 'authenticated': authenticated, "data": data, "driver_rides": driver_rides, "passenger_rides": passenger_rides})
    else:
        return render(request, "rides.html", {'user': user, 'authenticated': authenticated, 'data': "FAILED"})
    # driver_rides = [
    # {'date': 'Mar. 2 5PM', 'dropoff_number': 2, 'passenger_number': 3, 'available_seats': 2},
    # {'date': 'Mar. 5 5PM', 'dropoff_number': 1, 'passenger_number': 1, 'available_seats': 4},
    # ]
    # passenger_rides = [
    # {'driver': 'Jane Doe', 'date': 'Mar. 3 8PM', 'passenger_number': 3, 'dropoff_number': 2},
    # {'driver': 'Jane Doe', 'date': 'Mar. 12 3PM', 'passenger_number': 1, 'dropoff_number': 2},
    # ]"


@csrf_protect
@never_cache
@require_http_methods(["GET", "POST"])
def create_ride(request):
    user = "John Doe"
    context = {'user': user, "authenticated": True}
    if request.method == "POST":
        driver = 1
        open_seats = request.POST['open_seats']
        departure = request.POST['departure']
        data = {'driver': driver, 'open_seats': open_seats, 'departure': departure}
        url = experience + "create_ride/"
        response = requests.put(url, json=data)
        if response.status_code == HTTP_201_CREATED:
            data = response.json()
            ride_id = data['ride_id']
            available_seats = data['open_seats']
            departure = data["departure"]
            ride_status = 1
            driver = "John Doe"
            details = {"ride_id": ride_id, "available_seats": available_seats, "departure": departure, "ride_status": ride_status, "driver": driver}
            context['details'] = details
            context['data'] = data
            return redirect("ride_detail", int(ride_id))
        else:
            context['data'] = "FAILED"
            return redirect("dashboard")
    return render(request, "create_ride.html", context)
