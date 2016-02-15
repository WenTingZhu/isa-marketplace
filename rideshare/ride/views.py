from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json
from django.views.decorators.http import require_http_methods
from accounts.status_codes import *
from django.views.decorators.csrf import csrf_protect, csrf_exempt

from ride.models import Ride, RideRequest
from accounts.models import UserProfile

@csrf_exempt
@require_http_methods(["GET", "POST"])
def ride(request, id):
    if request.method == 'GET':
        try:
            ride = Ride.objects.get(pk=id)
            driver = UserProfile.objects.get(pk=ride.driver)
            passengers = ride.passengers.all()
            dropoffLocations = ride.dropoffLocations.all()
            data = {'ride-status': str(ride.status), 'dropOffLocations': str(dropOffLocations), 'passengers': str(passengers), 'departure': str(ride.departure), 'open-seats': str(ride.openSeats), 'driver':driver.user.first_name + driver.user.last_name, 'status': str(HTTP_200_OK)}
            return JsonResponse(data, status=HTTP_200_OK)
        except Ride.DoesNotExist:
            data = {'message': 'ride with id ' + id + ' was not found.', 'status': str(HTTP_404_NOT_FOUND)}
            return JsonResponse(data, status=HTTP_404_NOT_FOUND)
    else:
        html = "<html><body><h1>update ride</h1></body></html>"
        return HttpResponse(html)

@csrf_exempt
@require_http_methods(["GET", "POST"])
def ride_request(request, id):
    if request.method == 'GET':
        try:
            riderequest = RideRequest.objects.get(pk=id)
            data = {'ride': str(riderequest.ride.id), 'passenger': str(riderequest.passenger.id), 'driver-confirm': str(riderequest.driverConfirm), 'ride-confirm': str(riderequest.rideConfirm), 'status': str(HTTP_200_OK)}
            return JsonResponse(data, status=HTTP_200_OK)
        except Ride.DoesNotExist:
            data = {'message': 'ride request with id ' + id + ' was not found.', 'status': str(HTTP_404_NOT_FOUND)}
            return JsonResponse(data, status=HTTP_404_NOT_FOUND)
    else:
        html = "<html><body><h1>update ride</h1></body></html>"
        return HttpResponse(html)

@csrf_exempt
@require_http_methods(["PUT"])
def create_ride_request(request):
    data = json.loads(request.body.decode("utf-8"))
    ride = Ride.objects.get(pk=data['ride_id'])
    passenger = UserProfile.objects.get(pk=data['passenger_id'])

    new_ride_request = RideRequest.objects.create(ride=ride, passenger=passenger, driverConfirm=False, rideConfirm=False)
    new_ride_request.save()
    dataresult = {'status': str(HTTP_201_CREATED),'id': str(new_ride_request.id)}
    return JsonResponse(dataresult, status=HTTP_201_CREATED)

@csrf_exempt
@require_http_methods(["PUT"])
def create_ride(request):
    data = json.loads(request.body.decode("utf-8"))
    # driver = UserProfile.objects.get(user=request.user)
    new_ride = Ride.create(driver=data['driver'], openSeats=data['open_seats'], departure=data['departure'], status=0)
    new_ride.save()
    dataresult = {'status': str(HTTP_201_CREATED),'id': str(new_rid.id), 'open_seats': new_ride.openSeats, 'departure': new_ride.departure}
    return JsonResponse(dataresult, status=HTTP_201_CREATED)


# SERVICES  list
# GET
# - driver, open seats, departure time, status
# POST
# -
