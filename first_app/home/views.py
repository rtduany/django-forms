from django.shortcuts import render
#from django.http import HttpResponse
from .forms import StudentForm

# Create your views here.


def index(request):
	context = {
		"hello_message": "Register new student"
		"form": form
	}
	form = StudentForm(request.POST or None)
	if form.is_Valid():
		form.save()
	context = {
		"hello_message": "student saved"
		"form": form

	return render(request, 'index.html' , context)
