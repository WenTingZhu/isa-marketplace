from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_protect, csrf_exempt
import requests
from connector.status_codes import *

@csrf_exempt
@require_http_methods(["GET"])
def home():
    return  JsonResponse({}, status=HTTP_200_OK)

@csrf_exempt
@require_http_methods(["POST"])
def authenticate_user(request):
    data = json.loads(request.body.decode("utf-8"))
    url = authenticate_user_url(username, password)
    resp = requests.post(url)
    if resp.status == HTTP_202_ACCEPTED:
        return JsonResponse({'message': 'User authenticated'}, status=HTTP_202_ACCEPTED)
    else:
        return JsonResponse({'message': 'Invalid Login'}, status=HTTP_401_UNAUTHORIZED)

@csrf_exempt
@require_http_methods(["GET"])
def get_ride(requst, id):
    url = "http://models:8000/" + "api/v1/ride/ride/" + id +"/"
    resp = requests.get(url)
    if resp.status_code == HTTP_200_OK:
        data = resp.json();
        return JsonResponse({'message': 'Ride found', "data": data}, status=HTTP_200_OK)
    else:
        return JsonResponse({'message': 'Ride not found'}, status=HTTP_401_UNAUTHORIZED)

@csrf_exempt
@require_http_methods(["GET"])
def user_rides(requst, id):
    url = "http://models:8000/" + "api/v1/accounts/user/" + id + "/rides/"
    resp = requests.get(url)
    if resp.status_code == HTTP_200_OK:
        data = resp.json();
        return JsonResponse({'message': 'Ride found', "data": data}, status=HTTP_200_OK)
    else:
        return JsonResponse({'message': 'Ride not found'}, status=HTTP_401_UNAUTHORIZED)


@csrf_exempt
@require_http_methods(["PUT"])
def create_ride(request):
    """
    PUT http://experience:8001/create_ride/
    """
    data = json.loads(request.body.decode("utf-8"))
    # curl -H "Content-Type: application/json" -X PUT -d '{"driver":"1","open_seats":3, "departure": "2016-01-20 05:30"}' http://localhost:8000/api/v1/ride/ride/
    url = "http://models:8000/" + "api/v1/ride/ride/"
    resp = requests.put(url, json={"driver":data['driver'],"open_seats":data['open_seats'], "departure": data['departure']})
    if resp.status_code == HTTP_201_CREATED:
        new_ride = resp.json()
        return JsonResponse({'message': 'Ride Created', 'ride_id': new_ride['id'], 'open_seats': new_ride['open_seats'], 'departure': new_ride['departure']}, status=HTTP_201_CREATED)
    else:
        return JsonResponse({'message': 'Ride not found'}, status=HTTP_401_UNAUTHORIZED)


@csrf_exempt
@require_http_methods(['PUT'])
def create_account(request):
    """
    PUT
    """
    pass 

# SERVICES  list
# GET
# - driver, open seats, departure time, status
# POST
# -
