from django.db import models
# from django.contrib.auth.models import User

class UserProfile(models.Model):
	# user = models.OneToOneField(User)

	first_name = models.CharField(blank=True, max_length=50)
	last_name = models.CharField(blank=True, max_length=50)
	password = models.CharField(blank=True, max_length=50)
	email = models.CharField(blank=True, max_length=50, unique=True)

	phone = models.CharField(blank=True, max_length=10)
	school = models.CharField(blank=True, max_length=50)
	rating = models.DecimalField(blank=True, max_digits=2, decimal_places=1)

	# contains a Many-toMany to Ride

	def __str__(self):
		return self.email


class UserAuthenticator(models.Model):
	user = models.OneToOneField(UserProfile)
	authenticator = models.CharField(blank=True)
	date_created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return "{} : {}".format(str(self.user), self.authenticator )
