from django.test import TestCase
from accounts.models import UserProfile, UserAuthenticator
from django.contrib.auth.hashers import check_password, make_password
from decimal import Decimal, getcontext


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

    def verify_pword(self):
        """Verify password"""
        himanshu = UserProfile.objects.get(email='ho2es@virginia.edu')
        revanth = UserProfile.objects.get(email='rk8mt@virginia.edu')
        self.assertTrue(check_password('p', himanshu.password))
        self.assertTrue(check_password('p2', revanth.password))
