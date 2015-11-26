from django.db import models
class Agenda(models.Model):
	nombre = models.CharField(maxlength=30)
	apellido = models.CharField(maxlength=40)
	pais = models.CharField(maxlength=30)
	correo = models.EmailField()	
	
	def __str__(self):
		return ' %s %s' % (self.nombre, self.pais)
