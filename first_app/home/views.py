from django.shortcuts import render
#from django.http import HttpResponse
from .forms import StudentForm

# Create your views here.


def index(request):
	form = StudentForm(request.POST or None)
	if form.is_Valid():
		form.save()
	context = {
		"hello_message": "hello Moringa"
		"form": form
	}
	return render(request, 'index.html' , context)
