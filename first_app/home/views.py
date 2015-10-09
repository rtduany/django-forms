from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
	context = {
		"hello_message" : "hello Moringa"
	}
	return render(request, 'index.html' , context)
