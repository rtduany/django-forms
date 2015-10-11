from django import forms
from .models import student


class StudentForm(forms.ModelForm):
	class Meta:
		# fields = ['full_name', 'email', 'age']
		exclude = ['last_update']
		model = student

	def clean_age(self):
		age = self.cleaned_data.get('age')
		if age > 120:
			raise forms.validationError('you may be too old for this class')
		elif age < 10:
			raise forms.validationError('you may be young old for this class')
		return age

class FeedBackForm(forms.Form):
	full_name = forms.CharField()
	email = forms.EmailField()
	message = forms.CharField()
