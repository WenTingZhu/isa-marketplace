from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
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
    GET http://frontend:8000/
    """

    invalid_login = request.session.pop('invalid_login', False)

    #todo: redirect to dashboard if user is already authenticated
    # if request.user.is_authenticated():
        # return redirect('dashboard')

    signup_form = SignupForm()
    login_form = LoginForm()

    return render(request, "index.html", {
        "invalid_login": invalid_login,
        "authenticated": False,
        "signup_form": signup_form,
        "login_form": login_form,
        "redirect_possible": 'next' in request.GET
    })


@sensitive_post_parameters()
@csrf_protect
@never_cache
@require_http_methods(["POST"])
def create_user(request):
    """
    POST http://frontend:8002/create_user/
    """

    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            url = 'http://experience:8000/create_account/'
            data = {
                'email': form.cleaned_data['email'],
                'password': form.cleaned_data['password'],
                'first_name': form.cleaned_data['first_name'],
                'last_name': form.cleaned_data['last_name'],
                'phone': form.cleaned_data['phone'],
                'school': form.cleaned_data['school'],
            }
            resp = requests.put(url, json=data)
            if resp.status_code == HTTP_201_CREATED:
                user_id = resp.json()['user_id']
                url = 'http://experience:8000/authenticate_user/'
                resp = requests.post(url, json={
                    'email': form.cleaned_data['email'],
                    'password': form.cleaned_data['password'],
                })
                if resp.status_code == HTTP_202_ACCEPTED:
                    auth = resp.json()['authenticator']
                    request.session['authenticator'] = auth
                    request.session['email'] = form.cleaned_data['email']
                    request.session['user_id'] = user_id
                    return redirect('dashboard')
                else:
                    request.session['invalid_login'] = True
                    return HttpResponse('Created the user, but failed to authenticate:' + str(resp.content))
            else:
                return HttpResponse(str(resp.content))
        else:
            return HttpResponse(form.errors)
    return HttpResponse('failed')


@sensitive_post_parameters()
@csrf_protect
@never_cache
@require_http_methods(["POST"])
def login(request):
    """
    POST http://frontend:8002/login/
    """
    next_page = request.GET.get('next') or 'index'
    if request.method == "POST":
        form = LoginForm()
        if form.is_valid():
            # process data from form.cleaned_data
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            data = {'email': email, 'password': password}
            url = experience + "authenticate_user/"
            # Send request to experience and get response
            response = requests.post(
                url,
                data=json.dumps(data).encode('utf8'),
                headers={'content-type': 'application/json'}
            )

            if response.status_code == HTTP_202_ACCEPTED:
                auth = resp.json()['authenticator']
                user_id = resp.json()['user_id']
                request.session['authenticator'] = auth
                request.session['email'] = form.cleaned_data['email']
                request.session['user_id'] = user_id
                return redirect(next_page)
            else:
                request.session['invalid_login'] = True
                return redirect('index')
    return redirect('index')


def logout(request):
    # logout user
    del request.session['email']
    del request.session['authenticator']
    redirect('index')


# @login_required(login_url='/login')
def dashboard(request):
    # Grab user data
    user_id = request.session['user_id']
    url = experience + "user_detail/{user_id}/".format(user_id=user_id)
    context = {}
    response = requests.get(url, headers={'authenticator':request.session['authenticator'], 'email':request.session['email']})
    if response.status_code == HTTP_200_OK:
        data = response.json()
        context["full_name"] = data['first_name'] + " " + data['last_name']
        return render(request, "dashboard.html", context)
    else:
        return HttpResponse(str(response.content))
        next_url = '/?next=' + request.path
        return redirect(next_url)


def ride_detail(request, id):
    user = "John Doe"
    context = {'user': user, "authenticated": True}
    url = experience + "get_ride/" + id + "/"
    response = requests.get(url, headers={'authenticator':request.session['authenticator'], 'email':request.session['email']})
    if response.status_code == HTTP_200_OK:
        data = response.json()
        data = data["data"]
        context["details"] = data
        context["data"] = data
        return render(request, "ride-details.html", context)
    else:
        return HttpResponse(response.content)
        next_url = '/?next=' + request.path
        return redirect(next_url)


def rides(request):
    # invalid_login = request.session.pop('invalid_login', False)

    user = "John Doe"
    authenticated = True

    url = experience + "user_rides/1/"
    response = requests.get(url, headers={'authenticator':request.session['authenticator'], 'email':request.session['email']})
    if response.status_code == HTTP_200_OK:
        data = response.json()
        data = data["data"]
        driver_rides = json.loads(data["driver_rides"])
        passenger_rides = json.loads(data["passenger_rides"])

        return render(request, "rides.html", {
            'user': user,
            'authenticated': authenticated,
            "data": data,
            "driver_rides": driver_rides,
            "passenger_rides": passenger_rides
        })
    else:
        return HttpResponse(response.content)
        next_url = '/?next=' + request.path
        return redirect(next_url)


@csrf_protect
@never_cache
@require_http_methods(["GET", "POST"])
def create_ride(request):
    user = "John Doe"
    context = {'user': user, "authenticated": True}
    if request.method == "POST":
        form = CreateRideForm(data=request.POST)
        if form.is_valid():
            data = form.cleaned_data
            driver = 1
            open_seats = data['open_seats']
            departure = str(data['departure'])
            values = {'driver': driver, 'open_seats':
                      open_seats, 'departure': departure}
            url = experience + "create_ride/"
            response = requests.put(url, json=values, headers={'authenticator':request.session['authenticator'], 'email':request.session['email']})
            if response.status_code == HTTP_201_CREATED:
                data = response.json()
                ride_id = data['ride_id']
                available_seats = data['open_seats']
                departure = data["departure"]
                ride_status = 1
                driver = "John Doe"
                details = {
                    "ride_id": ride_id, "available_seats": available_seats,
                    "departure": departure, "ride_status": ride_status, "driver": driver}
                context['details'] = details
                context['data'] = data
                return redirect("ride_detail", int(ride_id))
            else:
                context['message'] = "Request Failed"
                context['message_details'] = response.text
                return render(request, "error.html", context)
        else:
            context['message'] = "Invalid Form Submission"
            context['message_details'] = "Open Seats: {}\nDeparture:{}".format(
                request.POST['open_seats'],
                request.POST['departure'],
            )
            return render(request, "error.html", context)
    create_ride_form = CreateRideForm()
    context['create_ride_form'] = create_ride_form
    return render(request, "create_ride.html", context)
