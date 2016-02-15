from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json
from django.views.decorators.http import require_http_methods
from accounts.status_codes import *
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.contrib.auth.models import User

from accounts.models import UserProfile
from ride.models import Ride

def home(request):
    html = "<html><head><title>Welcome to Rideshare!</title></head><body><h1>Welcome to Rideshare!</h1></body></html>"
    return HttpResponse(html)

# GET or UPDATE user
@csrf_exempt
@require_http_methods(["GET", "POST"])
def user(request, id):
    if request.method == 'GET':
        try:
            user = UserProfile.objects.get(pk=id)
            # rides = user.Ride_set.all()
            data = {'rating': str(user.rating), 'school': user.school, 'last_name': user.user.last_name, 'first_name': user.user.first_name, 'email': user.user.email, 'number': user.phone, 'id': str(id), 'status': str(HTTP_200_OK)}
            return JsonResponse(data, status=HTTP_200_OK)
        except UserProfile.DoesNotExist:
            data = {'message': 'user with id ' + id + ' was not found.', 'status': str(HTTP_404_NOT_FOUND)}
            return JsonResponse(data, status=HTTP_404_NOT_FOUND)
    else:
        data = json.loads(request.body.decode("utf-8"))
        try:
            user = UserProfile.objects.get(pk=id)
            if data['email']:
                user.user.email = data['email']
                user.user.username = data['email']
            if data['password']:
                user.user.password = data['password']
            if data['first_name']:
                user.user.first_name = data['first_name']
            if data['last_name']:
                user.user.email = data['last_name']
            if data['phone']:
                user.phone = data['phone']
            if data['school']:
                user.school = data['school']
            user.user.save()
            user.save()
        except UserProfile.DoesNotExist:
            data = {'message': 'user with id ' + id + ' was not found.', 'status': str(HTTP_404_NOT_FOUND)}
            return JsonResponse(data, status=HTTP_404_NOT_FOUND)

@csrf_exempt
@require_http_methods(["PUT"])
def create_user(request):
    data = json.loads(request.body.decode("utf-8"))
    new_user = User.objects.create_user(username=data['email'], email=data['email'], password=data['password'], first_name=data['first_name'], last_name=data['last_name'])
    new_user_profile = UserProfile(user=new_user, phone=data['phone'], school=data['school'], rating=0)
    new_user.save()
    new_user_profile.save()
    dataresult = {'status': str(HTTP_201_CREATED),'id': str(new_user_profile.id), 'email': new_user_profile.user.email, 'first_name': new_user_profile.user.first_name, 'last_name': new_user_profile.user.last_name, 'phone': new_user_profile.phone, 'school': new_user_profile.school, 'rating': str(new_user_profile.rating)}
    return JsonResponse(dataresult, status=HTTP_201_CREATED)


# SERVICES  list
# GET
# - name, email, number, school/university, rating (id)
# POST
# - create user (name, email, password, phone, school, rating)
# - update user (name, email, password, phone, school, rating)
