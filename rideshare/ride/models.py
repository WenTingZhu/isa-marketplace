from django.db import models
from accounts.models import UserProfile

STATUS_CHOICES = (
	(0, 'open'),
	(1, 'full'),
	(2, 'departed'),
	(3, 'completed'),
)

class Ride(models.Model):
	driver = models.ForeignKey(UserProfile, null=True)
	openSeats = models.IntegerField()
	departure = models.DateTimeField()
	status = models.IntegerField(choices=STATUS_CHOICES)
	passenger = models.ManyToManyField(UserProfile)
	dropoffLocation = models.ManyToManyField(DropoffLocation)


class RideRequest(models.Model):
	passenger = models.ForeignKey(UserProfile, null=True)
	ride = models.ForeignKey(Ride, null=True)
	driverConfirm = models.BooleanField()
	rideConfirm = models.BooleanField()

class DropoffLocation(models.Model):
	name = models.CharField(max_length=500)
	address = models.CharField(max_length=500)
	city = models.CharField(max_length=100)
	state = models.CharField(max_length=2)
	zipcode = models.IntegerField()
