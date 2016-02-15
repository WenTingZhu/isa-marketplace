from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json
from django.views.decorators.http import require_http_methods
from accounts.status_codes import *
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.contrib.auth.models import User

from accounts.models import UserProfile

def home(request):
    html = "<html><head><title>Welcome to Rideshare!</title></head><body><h1>Welcome to Rideshare!</h1></body></html>"
    return HttpResponse(html)

# GET or UPDATE user
@csrf_protect
@require_http_methods(["GET", "POST"])
def user(request, id):
    if request.method == 'GET':
        try:
            user = UserProfile.objects.get(pk=id)
            data = {'status': str(HTTP_200_OK), 'id': str(id), 'email': user.user.email, 'first_name': user.user.first_name, 'last_name': user.user.last_name, 'number': user.phone, 'school': user.school, 'rating': str(user.rating)}
            return JsonResponse(data, status=HTTP_200_OK)
        except UserProfile.DoesNotExist:
            data = {'status': str(HTTP_404_NOT_FOUND), 'message': 'user with ' + id + ' was not found.'}
            return JsonResponse(data, status=HTTP_404_NOT_FOUND)

@csrf_exempt
@require_http_methods(["PUT"])
def create_user(request):    
    data = json.loads(request.body.decode("utf-8"))
    new_user = User.objects.create_user(username=data['email'], email=data['email'], password=data['password'], first_name=data['first_name'], last_name=data['last_name'])
    new_user_profile = UserProfile(user=new_user, phone=data['phone'], school=data['school'], rating=0)

    new_user_profile.save()
    dataresult = {'status': str(HTTP_201_CREATED),'id': str(new_user_profile.id), 'email': new_user_profile.user.email, 'first_name': new_user_profile.user.first_name, 'last_name': new_user_profile.user.last_name, 'phone': new_user_profile.phone, 'school': new_user_profile.school, 'rating': str(new_user_profile.rating)}
    return JsonResponse(dataresult, status=HTTP_201_CREATED)



# SERVICES  list
# GET
# - name, email, number, school/university, rating (id)
# POST
# - create user (name, email, password, phone, school, rating)
# - update user (name, email, password, phone, school, rating)
