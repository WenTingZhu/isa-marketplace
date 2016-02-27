from furl import furl
BASE = 'http://localhost'
PORT = 8000
API_PATH = ["api", "v1"]

f = furl(BASE)
f.port = PORT
f.fragement.path.segments = API_PATH


def authenticate_user(user_id):
    return f.copy().fragment.path.segments.extend(["accounts", "user", "authenticate", str(user_id)]).url

# def get_user(user_id):
#     return f.copy().fragment.path.segments.extend(["accounts", "user", str(user_id)]).url

# def create_user():
#     return f.copy().fragment.path.segments.extend(["accounts", "user", str(user_id)]).url

# def delete_user():
#     return
#
# def get_ride(ride_id):
#     return "".format(user_id)
#
# def create_ride():
#     return
#
# def delete_ride():
#     return
#
#
#
#
#     url(r'^user/$', views.create_user, name='create_user'),
#     url(r'^user/(\d+)/$', views.user, name='user'),
#     url(r'^user/delete/(\d+)/$', views.delete_user, name='delete_user'),
#
#         url(r'^ride/$', views.create_ride, name='create_ride'),
#         url(r'^ride/delete/(\d+)/$', views.delete_ride, name='delete_ride'),
#         url(r'^ride/(\d+)/$', views.ride, name='ride'),
#         url(r'^rideRequest/(\d+)/$', views.ride_request, name='ride_request'),
#         url(r'^rideRequest/$', views.create_ride_request, name='create_ride_request'),
