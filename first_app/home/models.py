from django.db import models

# Create your models here.


class classroom(models.Model):
	name = models.CharField(max_length=40)
	floor = models.CharField(max_length=20)
	has_podium = models.CharField(max_length=20)
	commissioned_date = models.DateTimeField('date commissioned')
	created_at = models.TimeField(_(u"Created Time"), auto_now_add=True, blank=True)
	updated_at = models.TimeField(_(u"Updated Time"), auto_now_add=True, blank=True)
