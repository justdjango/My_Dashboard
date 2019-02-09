from django.conf import settings
from django.db import models
from django.urls import reverse

class Note(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	title = models.CharField(max_length=120)
	image = models.ImageField(null=True, blank=True)
	url = models.URLField(null=True, blank=True)
	timestamp = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title

	def get_delete_url(self):
		return reverse("notes:delete", kwargs={
			"id": self.id
		})
	
	def get_update_url(self):
		return reverse("notes:update", kwargs={
			"id": self.id
		})