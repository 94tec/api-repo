from django.db import models

class Employee(models.Model):
	name = models.CharField(max_length=255)
	email = models.EmailField(max_length=255)
	job = models.CharField(max_length=255)
	salary = models.PositiveIntegerField()
	created = models.DateField(auto_now_add=True)

	def __str__(self) -> str:
		return self.name
