from datetime import datetime
from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.signals import post_save

User = get_user_model()

class Headline(models.Model):
	title = models.CharField(max_length=120)
	image = models.ImageField()
	url = models.TextField()

	def __str__(self):
		return self.title

class UserProfile(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	last_scrape = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return "{}-{}".format(self.user, self.last_scrape)


def post_user_signup_receiver(sender, instance, **kwargs):
	userprofile, created = UserProfile.objects.get_or_create(user=instance)

post_save.connect(post_user_signup_receiver, sender=User)