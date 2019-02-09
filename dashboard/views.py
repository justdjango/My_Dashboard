import math
from datetime import timedelta, timezone, datetime
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from notepad.forms import NoteModelForm
from notepad.models import Note
from news.models import Headline, UserProfile

@login_required
def home(request):
	user_p = UserProfile.objects.get(user=request.user)
	now = datetime.now(timezone.utc)
	time_difference = now - user_p.last_scrape
	time_difference_in_hours = time_difference / timedelta(minutes=60)
	next_scrape = 24 - time_difference_in_hours
	if time_difference_in_hours <= 24:
		hide_me = True
	else:
		hide_me = False

	headlines = Headline.objects.all()

	notes = Note.objects.filter(user=request.user)

	form = NoteModelForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		form.instance.user = request.user
		form.save()
		return redirect('/home/')

	context = {
		'form': form,
		'notes_list': notes,
		'object_list': headlines,
		'hide_me': hide_me,
		'next_scrape': math.ceil(next_scrape)
	}

	return render(request, "news/home.html", context)



