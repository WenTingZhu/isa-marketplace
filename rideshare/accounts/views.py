from django.shortcuts import render
from django.http import HttpResponse
import json
from django.views.decorators.http import require_http_methods

from accounts.models import UserProfile

def home(request):
    html = "<html><head><title>Welcome to Rideshare</title></head><body><h1>Welcome to Rideshare!</h1></body></html>"
    return HttpResponse(html)

# GET or UPDATE user
@require_http_methods(["GET", "POST"])
def user(request, id):
    if request.method == 'GET':
        try:
            user = UserProfile.objects.get(pk=id)
            response = {'status': str(200), 'id': str(id), 'email': user.user.email, 'first_name': user.user.first_name, 'last_name': user.user.last_name, 'number': user.phone, 'school': user.school, 'rating': str(user.rating)}
            return HttpResponse(json.dumps(response), content_type='application/json')
        except UserProfile.DoesNotExist:
            response = {'status': '404', 'message': 'User with given user id was not found.'}
            return HttpResponse(json.dumps(response), content_type='application/json')
    else: # request.method == 'POST':
        # do_something_else
        data = json.loads(request.body)
        return HttpResponse(json.dumps(data), content_type='application/json')



# SERVICES  list
# GET
# - name, email, number, school/university, rating (id)
# POST
# - create user (name, email, password, phone, school, rating)
# - update user (name, email, password, phone, school, rating)
