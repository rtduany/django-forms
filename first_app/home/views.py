from django.shortcuts import render
from .forms import StudentForm
from .forms import FeedBackForm

# Create your views here.


def index(request):
	form = StudentForm(request.POST or None)

	context = {
		"hello_message": "Register new student",
		"form": form
	}

	if form.is_valid():
		instance = form.save(commit=False)
		full_name = form.cleaned_data.get('full_name')
		if full_name == "ruot":
			full_name == "Software Engineer"
		instance.full_name = full_name
		instance.save()

	context = {
		"hello_message": "student saved",
	}

	return render(request, 'index.html' , context)

def feedback(request):
		form = FeedBackForm(request.POST or None)
		if form.is_valid():
			for key, value in form.cleaned_data_iteritems():
				print(key, value)
		context = {
			"form": form
		}
		return render(request, 'feedback.html' , context)
