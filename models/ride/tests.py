from django.test import TestCase
from ride.models import Ride, RideRequest, DropoffLocation
from accounts.models import UserProfile
from decimal import Decimal, getcontext
from django.test import Client
from accounts.status_codes import *
import json


class RideTestCase(TestCase):
    def setUp(self):
        UserProfile.objects.create(first_name="Himanshu", last_name="Ojha", email="ho2es@virginia.edu", phone="703-953-1414", school="uva", rating=4, password='sd')
        self.himanshu = UserProfile.objects.get(email='ho2es@virginia.edu')
        UserProfile.objects.create(first_name="passenger guy", last_name="Ojha", email="ho3es@virginia.edu", phone="703-953-1434", school="uva", rating=4, password='sdd')
        # self.passenger = UserProfile.objects.get(email='ho3es@virginia.edu', openSeats=1)


    def test_add_passenger_to_ride(self):
        ride= Ride.objects.create(openSeats=3, departure='1994-12-11 11:11', status=0, )
        ride.passenger=[self.himanshu]
        ride.save()
        self.assertEqual(1, len(ride.passenger.all()))
        self.assertEqual(self.himanshu, ride.passenger.all()[0])

class CreateRideViewTestCase(TestCase):
    def setUp(self):
        self.himanshu = UserProfile.objects.create(first_name="Himanshu", last_name="Ojha", email="ho2es@virginia.edu", phone="703-953-1414", school="uva", rating=4, password='sd')

    def test_create_ride_view(self):
        c= Client()
        c.put('/api/v1/ride/ride/', json.dumps({'driver':self.himanshu.id, 'open_seats':1,'departure':'1994-12-11 11:11'}))
        ride = Ride.objects.get(driver=self.himanshu.id)
        self.assertTrue(ride != None )

    def test_get_ride_view(self):
        c=Client()
        c.put('/api/v1/ride/ride/', json.dumps({'driver':self.himanshu.id, 'open_seats':1,'departure':'1994-12-11 11:11'}))
        ride = Ride.objects.get(driver=self.himanshu.id)

        response = c.get('/api/v1/ride/ride/{}/'.format(ride.id))
        self.assertEqual(response.status_code, HTTP_200_OK)
        data = json.loads(response.content.decode('utf-8'))
        self.assertEqual(data['ride_status'], '0')
        self.assertEqual(data['dropoffLocations'], [])
        self.assertEqual(data['passengers'], '[]')
        self.assertEqual(data['departure'], 'Dec 11, 1994 11:11')
        self.assertEqual(data['available_seats'], '1')
        self.assertEqual(data['driver_email'], 'ho2es@virginia.edu')
        self.assertEqual(data['status'], str(HTTP_200_OK))


class AllRideViewTestCase(TestCase):
    def setUp(self):
        self.himanshu = UserProfile.objects.create(first_name="Himanshu", last_name="Ojha", email="ho2es@virginia.edu", phone="703-953-1414", school="uva", rating=4, password='sd')


    def test_all_rides_empty(self):
        Ride.objects.all().delete()
        c=Client()
        response = c.get('/api/v1/ride/ride/rides/')
        data = json.loads(response.content.decode('utf-8'))['rides_list']
        rides_list = json.loads(data)
        self.assertEqual(len(rides_list), 0)

    def test_all_rides_non_empty(self):
        Ride.objects.all().delete()
        c=Client()
        c.put('/api/v1/ride/ride/', json.dumps({'driver':self.himanshu.id, 'open_seats':1,'departure':'1994-12-11 11:11'}))
        c.put('/api/v1/ride/ride/', json.dumps({'driver':self.himanshu.id, 'open_seats':3,'departure':'1994-12-11 12:11'}))
        response = c.get('/api/v1/ride/ride/rides/')
        data = json.loads(response.content.decode('utf-8'))['rides_list']
        rides_list = json.loads(data)
        self.assertEqual(len(rides_list), 2)





# class CreateRideViewTestCase(TestCase):
