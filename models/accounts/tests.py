from django.test import TestCase
from accounts.models import UserProfile, UserAuthenticator
from django.contrib.auth.hashers import check_password, make_password
from decimal import Decimal, getcontext
from django.test import Client
from accounts.status_codes import *
import json


class UserProfileTestCase(TestCase):
    def setUp(self):
        p = make_password('p')
        UserProfile.objects.create(first_name="Himanshu", last_name="Ojha", email="ho2es@virginia.edu", phone="703-953-1414", school="uva", rating=4, password=p)
        p = make_password('p2')
        UserProfile.objects.create(first_name="Revanth", last_name="Kolli", email="rk8mt@virginia.edu", phone="234-333-3433", school="uva", rating=5, password=p)
        p = make_password('p3')
        UserProfile.objects.create(first_name="Loco Man", last_name="Kolli", email="loco@virginia.edu", phone="234-333-3433", school="uva", rating=1, password=p)
        p = make_password('p5')
        UserProfile.objects.create(first_name="Wendy", last_name="Zhu", email="wendy@virginia.edu", phone="234-333-3433", school="uva", rating=9.3, password=p)
        p = make_password('p12')
        UserProfile.objects.create(first_name="moco", last_name="Kolli", email="moco@harvard.edu", phone="234-333-3433", school="harvard", rating=4.3, password=p)
        p = make_password('p12')
        UserProfile.objects.create(first_name="coco", last_name="Kolli", email="coco@coco.edu", phone="234-333-3433", school="coco", rating=5.2, password=p)

    def test_proper_password(self):
        """UserProfile password initialization"""
        loco = UserProfile.objects.get(email="loco@virginia.edu")
        coco = UserProfile.objects.get(email="coco@coco.edu")
        moco = UserProfile.objects.get(email="moco@harvard.edu")
        self.assertTrue(check_password('p3', loco.password))
        self.assertTrue(check_password('p12', coco.password))
        self.assertTrue(check_password('p12', moco.password))

    def test_rating(self):
        """UserProfile password initialization is blank"""
        loco = UserProfile.objects.get(email="loco@virginia.edu")
        coco = UserProfile.objects.get(email="coco@coco.edu")
        moco = UserProfile.objects.get(email="moco@harvard.edu")
        # getcontext().prec = 2
        self.assertEqual(coco.rating, Decimal("5.2"))
        self.assertEqual(loco.rating, Decimal("1"))
        self.assertEqual(moco.rating, Decimal("4.3"))


class UserAuthenticatorTestCase(TestCase):
    def setUp(self):
        p = make_password('p')
        UserProfile.objects.create(first_name="Himanshu", last_name="Ojha", email="ho2es@virginia.edu", phone="703-953-1414", school="uva", rating=4, password=p)
        p = make_password('p2')
        UserProfile.objects.create(first_name="Revanth", last_name="Kolli", email="rk8mt@virginia.edu", phone="234-333-3433", school="uva", rating=5, password=p)

    def test_verify_pword(self):
        """Verify password"""
        himanshu = UserProfile.objects.get(email='ho2es@virginia.edu')
        revanth = UserProfile.objects.get(email='rk8mt@virginia.edu')
        self.assertTrue(check_password('p', himanshu.password))
        self.assertTrue(check_password('p2', revanth.password))


class UserViewTestCase(TestCase):
    def setUp(self):
        p = make_password('p')
        UserProfile.objects.create(first_name="Himanshu", last_name="Ojha", email="ho2es@virginia.edu", phone="703-953-1414", school="uva", rating=4, password=p)

    def test_create_basic_user(self):
        c = Client()
        new_user_data = {
            'email':'ho2es@gmail.com',
            'password':'temp',
            'first_name':'himanshu',
            'last_name':'last_name',
            'phone':'123456789',
            'school':'uva',
        }
        response = c.put('/api/v1/accounts/user/', data=json.dumps(new_user_data), content_type='application/json')
        self.assertEqual(response.status_code, HTTP_201_CREATED)

    # def test_create_user_with_no_email(self):
    #     c = Client()
    #     new_user_data = {
    #         'email':'',
    #         'password':'temp',
    #         'first_name':'himanshu',
    #         'last_name':'last_name',
    #         'phone':'123456789',
    #         'school':'uva'
    #     }
    #     response = c.put('/api/v1/accounts/user/', new_user_data)
    #     self.assertEqual(response.status_code, HTTP_404_NOT_FOUND)

    # def test_create_user_with_too_long_phone(self):
    #     c = Client()
    #     new_user_data = {
    #         'email':'sdf@sdfgd.com',
    #         'password':'temp',
    #         'first_name':'himanshu',
    #         'last_name':'last_name',
    #         'phone':'1234335688888888888789',
    #         'school':'uva'
    #     }
    #     response = c.put('/api/v1/accounts/user/', json.dumps(new_user_data))
    #     self.assertEqual(response.status_code, HTTP_404_NOT_FOUND)


    def test_stored_password_is_not_simple_text(self):
        c = Client()
        email = 'sdddf@sdfgd.com'
        pword = 'temp'
        new_user_data = {
            'email':email,
            'password':pword,
            'first_name':'himanshu',
            'last_name':'last_name',
            'phone':'1356789',
            'school':'uva',
        }
        response = c.put('/api/v1/accounts/user/', json.dumps(new_user_data))
        self.assertEqual(response.status_code, HTTP_201_CREATED)
        user = UserProfile.objects.get(email=email)
        self.assertTrue(check_password(pword, user.password))

    def test_authenticate_user(self):
        c = Client()
        email = "rocko@adsf.com"
        pword = 'why not'
        new_user_data = {
            'email':email,
            'password':pword,
            'first_name':'himanshu',
            'last_name':'last_name',
            'phone':'1356789',
            'school':'uva',
        }
        c.put('/api/v1/accounts/user/', json.dumps(new_user_data))
        response = c.post('/api/v1/accounts/user/authenticate/', json.dumps({'email':email, 'password':pword}), content_type='application/json')
        self.assertEqual(response.status_code, HTTP_202_ACCEPTED)

        authenticator = json.loads(response.content.decode('utf-8'))['authenticator']
        response = c.post('/api/v1/accounts/user/authenticate/verify/', json.dumps({'authenticator':authenticator}), content_type='application/json')
        self.assertEqual(response.status_code, HTTP_202_ACCEPTED)

    def test_unauthenticate_user(self):
        c = Client()
        email = "rocko@adsf.com"
        pword = 'why not'
        new_user_data = {
            'email':email,
            'password':pword,
            'first_name':'himanshu',
            'last_name':'last_name',
            'phone':'1356789',
            'school':'uva',
        }
        c.put('/api/v1/accounts/user/', json.dumps(new_user_data))
        response = c.post('/api/v1/accounts/user/authenticate/', json.dumps({'email':email, 'password':pword}), content_type='application/json')
        self.assertEqual(response.status_code, HTTP_202_ACCEPTED)

        authenticator = json.loads(response.content.decode('utf-8'))['authenticator']
        response = c.post('/api/v1/accounts/user/authenticate/verify/', json.dumps({'authenticator':authenticator}), content_type='application/json')
        self.assertEqual(response.status_code, HTTP_202_ACCEPTED)


    def test_get_user(self):
        c = Client()
        email = "ho2es@virginia.edu"
        himanshu = UserProfile.objects.get(email=email)
        response = c.get('/api/v1/accounts/user/{}/'.format(himanshu.id))
        self.assertEqual(response.status_code, HTTP_200_OK)

        data = json.loads(response.content.decode('utf-8'))
        self.assertEqual(data['rating'], str(himanshu.rating))
        self.assertEqual(data['school'], himanshu.school)
        self.assertEqual(data['last_name'], himanshu.last_name)
        self.assertEqual(data['first_name'], himanshu.first_name)
        self.assertEqual(data['email'], himanshu.email)
        self.assertEqual(data['number'], himanshu.phone)
        self.assertEqual(int(data['id']), himanshu.id)

    def test_user_rides(self):
        c=Client()
        email ='ho2es@virginia.edu'
        himanshu = UserProfile.objects.get(email=email)
        c.put('/api/v1/ride/ride/', )
        response = c.get('/api/v1/accounts/user/{}/rides/'.format(himanshu.id))
