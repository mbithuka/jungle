from django.db import models

class Miti(models.Model):
	name = models.CharField(max_length = 200)
	quantity = models.IntegerField()
	price = models.DecimalField(max_digits = 23,decimal_places=2)

	def __str__(self):
		return self.name

