from django.contrib import admin

# Register your models here.
from .models import Headline, UserProfile

admin.site.register(Headline)
admin.site.register(UserProfile)