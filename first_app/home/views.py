from django.shortcuts import render
from django.http import ttpResponse
# Create your views here.


def index(request):
	return HttpResponse("success")