from django.db import models

# Create your models here.


class classroom(models.Model):
	name = models.CharField(max_length=200)
	floor = models.CharField(max_length=20)
	has_podium = models.CharField(max_length=20)
	commissioned_date = models.DateTimeField('date commissioned')
	created_at = models.TimeField(auto_now=False, auto_now_add=True)
	updated_at = models.TimeField(auto_now_add=True, blank=False)


	def __str__():
		return slf.full_name
