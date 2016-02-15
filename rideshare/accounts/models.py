from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
	user = models.OneToOneField(User)
	phone = models.CharField(blank=True, max_length=10)
	school = models.CharField(blank=True, max_length=50)
	rating = models.DecimalField(blank=True, max_digits=2, decimal_places=1)

	def __str__(self):
		return self.user.username
