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

    # redirect to dashboard if user is already authenticated
    if 'authenticator' in request.session and 'email' in request.session:
        resp = requests.get('http://experience:8000/verify_authenticator/', headers={'authenticator':request.session['authenticator'], 'email':request.session['email']})
        if resp.status_code == HTTP_200_OK:
            return redirect('dashboard')

    signup_form = SignupForm()
    login_form = LoginForm()
    search_form = SearchForm()

    return render(request, "index.html", {
        "invalid_login": invalid_login,
        "authenticated": False,
        "signup_form": signup_form,
        "login_form": login_form,
        "search_form": search_form,
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
                    return redirect('error')
            else:
                return HttpResponse(resp.content)
                return redirect('error')
        else:
            return redirect('error')
    return redirect('error')

@csrf_protect
@require_http_methods(['GET'])
def error(request):
    msg = request.GET.get('message','Internal Server Error')
    signup_form = SignupForm()
    login_form = LoginForm()
    search_form = SearchForm()
    return render(request, 'error.html', {'message':msg, 'signup_form': signup_form, 'login_form': login_form, 'search_form': search_form})

@sensitive_post_parameters()
@csrf_protect
@never_cache
@require_http_methods(["POST"])
def login(request):
    """
    POST http://frontend:8002/login/
    """
    next_page = request.GET.get('next') or 'dashboard'
    if request.method == "POST":
        form = LoginForm(request.POST)
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
                auth = response.json()['authenticator']
                user_id = response.json()['user_id']
                request.session['authenticator'] = auth
                request.session['email'] = form.cleaned_data['email']
                request.session['user_id'] = user_id
                return redirect(next_page)
            else:
                request.session['invalid_login'] = True
                return redirect('error')
        else:
            return redirect('error')
    return redirect('error')


def logout(request):
    if 'email' not in request.session or 'authenticator' not in request.session:
        return redirect('index')
    # logout user
    del request.session['email']
    del request.session['authenticator']
    # ignore result
    requests.post(experience+'unauthenticate_user/')

    return redirect('index')


# @login_required(login_url='/login')
def dashboard(request):
    if 'email' not in request.session or 'authenticator' not in request.session:
        return redirect('index')

    # Grab user data
    user_id = request.session['user_id']
    url = experience + "user_detail/{user_id}/".format(user_id=user_id)
    context = {}
    response = requests.get(
        url, headers={'authenticator': request.session['authenticator'], 'email': request.session['email']})
    if response.status_code == HTTP_200_OK:
        data = response.json()
        # raise Exception(data)
        context["full_name"] = data['first_name'] + " " + data['last_name']
        context['first_name'] = data['first_name']
        context['all_rides'] = []
        context['authenticated'] = True
        url = experience + "all_rides/"
        response = requests.get(
            url, headers={'authenticator': request.session['authenticator'], 'email': request.session['email']})
        if response.status_code == HTTP_200_OK:
            data = response.json()['data']
            all_rides = json.loads(data['rides_list'])
            context['all_rides'] = all_rides
        context['search_form'] = SearchForm()
        return render(request, "dashboard.html", context)
    else:
        return redirect('error')


def ride_detail(request, id):
    if 'email' not in request.session or 'authenticator' not in request.session:
        return redirect('index')
    context = {}
    url = experience + "get_ride/" + id + "/"
    response = requests.get(
        url, headers={'authenticator': request.session['authenticator'], 'email': request.session['email']})
    if response.status_code == HTTP_200_OK:
        data = response.json()
        data = data["data"]
        context["details"] = data
        context["data"] = data
        url = experience + "user_detail/{user_id}/".format(user_id=request.session['user_id'])
        resp = requests.get(
            url, headers={'authenticator': request.session['authenticator'], 'email': request.session['email']})
        if resp.status_code == HTTP_200_OK:
            data = resp.json()
            context["full_name"] = data['first_name'] + " " + data['last_name']
            context['first_name'] = data['first_name']
        else:
            context['full_name'] = 'Account'
        context['authenticated'] = True
        context['search_form'] = SearchForm()
        return render(request, "ride-details.html", context)
    else:
        return redirect('error')



def rides(request):
    if 'email' not in request.session or 'authenticator' not in request.session:
        return redirect('index')
    # invalid_login = request.session.pop('invalid_login', False)
    user_id = request.session['user_id']
    url = experience + "user_rides/{}/".format(user_id)
    response = requests.get(
        url, headers={'authenticator': request.session['authenticator'], 'email': request.session['email']})
    if response.status_code == HTTP_200_OK:
        data = response.json()
        # raise Exception(data)
        data = data["data"]
        driver_rides = json.loads(data["driver_rides"])
        passenger_rides = json.loads(data["passenger_rides"])
        url = experience + "user_detail/{user_id}/".format(user_id=user_id)
        resp = requests.get(
            url, headers={'authenticator': request.session['authenticator'], 'email': request.session['email']})
        if resp.status_code == HTTP_200_OK:
            data = resp.json()
            full_name = data['first_name'] + ' ' + data['last_name']
        else:
            full_name = 'Account'
        authenticated = True
        return render(request, "rides.html", {
            'full_name': full_name,
            'first_name': resp.json()['first_name'],
            'authenticated': authenticated,
            "driver_rides": driver_rides,
            "passenger_rides": passenger_rides,
            "search_form": SearchForm()
        })
    else:
        return redirect('error')



@csrf_protect
@never_cache
@require_http_methods(["GET", "POST"])
def create_ride(request):
    if 'email' not in request.session or 'authenticator' not in request.session:
        return redirect('index')

    user_id = request.session['user_id']
    context = {}
    if request.method == "POST":
        form = CreateRideForm(data=request.POST)
        if form.is_valid():
            data = form.cleaned_data

            open_seats = data['open_seats']
            departure = str(data['departure'])
            values = {
                'driver': user_id,
                'open_seats': open_seats,
                'departure': departure
            }
            url = experience + "create_ride/"
            response = requests.put(
                url,
                json=values,
                headers={
                    'authenticator': request.session['authenticator'],
                    'email': request.session['email']
                }
            )
            if response.status_code == HTTP_201_CREATED:
                data = response.json()
                ride_id = data['ride_id']
                available_seats = data['open_seats']
                departure = data["departure"]
                details = {
                    "ride_id": ride_id,
                    "available_seats": available_seats,
                    "departure": departure,
                    "ride_status": 1,
                    "driver": user_id
                }
                context['details'] = details
                context['data'] = data
                return redirect("ride_detail", int(ride_id))
            else:
                return redirect('error')
        else:
            return redirect('error')
    create_ride_form = CreateRideForm()
    context['create_ride_form'] = create_ride_form
    context['search_form'] = SearchForm()
    return render(request, "create_ride.html", context)

@csrf_protect
@never_cache
@require_http_methods(["POST"])
def search(request):
    form = SearchForm(data=request.POST)
    if form.is_valid():
        data = form.cleaned_data
    url = experience + 'search/'
    resp = requests.post(url, json={'query': data['query']})
    if resp.status_code == HTTP_200_OK:
        return HttpResponse(resp.content)
    else:
        return HttpResponse('FAILED' + str(resp.content))
        # todo: give some error message to user without breaking page

@csrf_protect
@never_cache
@require_http_methods(["POST"])
def search_results(request):
    context = {}
    if request.method == "POST":
        form = SearchForm(data=request.POST)
        if form.is_valid():
            data = form.cleaned_data
            context['query'] = data['query']
            context['search_form'] = SearchForm()
            return render(request, "results.html", context)
        else:
            return HttpResponse('2')
            return redirect('error')
    else:
        return HttpResponse('6')
        return redirect('error')
