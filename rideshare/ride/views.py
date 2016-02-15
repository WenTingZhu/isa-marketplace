from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json
from django.views.decorators.http import require_http_methods
from accounts.status_codes import *
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import csrf_exempt

from ride.models import Ride
from accounts.models import UserProfile

@csrf_exempt
@require_http_methods(["GET", "POST"])
def ride(request, id):
    if request.method == 'GET':
        try:
            ride = Ride.objects.get(pk=id)
            driver = UserProfile.objects.get(pk=ride.driver)
            data = {'ride-status': str(ride.status), 'departure': str(ride.departure), 'open-seats': str(ride.openSeats), 'driver':driver.user.first_name + driver.user.last_name, 'status': str(HTTP_200_OK)}
            return JsonResponse(data, status=HTTP_200_OK)
        except Ride.DoesNotExist:
            data = {'message': 'ride with id ' + id + ' was not found.', 'status': str(HTTP_404_NOT_FOUND)}
            return JsonResponse(data, status=HTTP_404_NOT_FOUND)
    else:
        html = "<html><body><h1>update ride</h1></body></html>"
        return HttpResponse(html)


@csrf_exempt
@require_http_methods(["PUT"])
def create_ride(request):
    data = json.loads(request.body.decode("utf-8"))
    new_ride = Ride.create(username=data['email'], email=data['email'], password=data['password'], first_name=data['first_name'], last_name=data['last_name'])
    new_ride.save()
    dataresult = {'status': str(HTTP_201_CREATED),'id': str(new_user_profile.id), 'email': new_user_profile.user.email, 'first_name': new_user_profile.user.first_name, 'last_name': new_user_profile.user.last_name, 'phone': new_user_profile.phone, 'school': new_user_profile.school, 'rating': str(new_user_profile.rating)}
    return JsonResponse(dataresult, status=HTTP_201_CREATED)



# SERVICES  list
# GET
# - driver, open seats, departure time, status
# POST
# -
