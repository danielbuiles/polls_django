import datetime
from django.db import models
from django.utils import timezone

# Create your models here.
class Preguntas(models.Model):
    pregunta = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.pregunta
    
    def publicado_recientemente(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    
class Opciones(models.Model):
    pregunta = models.ForeignKey(Preguntas, on_delete=models.CASCADE)
    opcion = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.opcion