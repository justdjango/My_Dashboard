from django.shortcuts import render, redirect

# Create your views here.

from .forms import NoteForm

# CRUD - create update retrieve and delete

def createView(request):
	form = NoteForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		form.instance.user = request.user
		form.save()
		return redirect('/')

	context = {
		'form': form
	}

	return render(request, "notepad/create.html", context)