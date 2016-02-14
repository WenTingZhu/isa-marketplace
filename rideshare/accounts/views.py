from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json
from django.views.decorators.http import require_http_methods
from accounts.status_codes import *
from django.views.decorators.csrf import csrf_protect


from accounts.models import UserProfile

def home(request):
    html = "<html><head><title>Welcome to Rideshare</title></head><body><h1>Welcome to Rideshare!</h1></body></html>"
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
            pass

@require_http_methods(["PUT"])
def create_user(request):
    return JsonResponse({'ok', 'it worked'})
    # new_user = User.objects.create_user(request.POST['username'], email=request.POST['email'], password=request.POST['password'], **request.POST)
    # new_user_profile = UserProfile(user=user, phone=request.POST['phone'], school=request.POST['school'], rating=request.POST['rating'])
    # new_user_profile.save()
    # data = {'status': str(HTTP_201_CREATED),'id': str(new_user_profile.id), 'email': new_user_profile.email, 'first_name': new_user_profile.first_name, 'last_name': new_user_profile.last_name, 'number': new_user_profile.phone, 'school': new_user_profile.school, 'rating': str(new_user_profile.rating)}
    # return JsonResponse(data, status=HTTP_201_CREATED)


# SERVICES  list
# GET
# - name, email, number, school/university, rating (id)
# POST
# - create user (name, email, password, phone, school, rating)
# - update user (name, email, password, phone, school, rating)
