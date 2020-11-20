from django.db import models
from editoriales.models import Editorial

class Libro(models.Model):
    nombre: models.CharField(max_length=200)
    fecha_publicacion: models.DateField()
    paginas: models.IntegerField()
    
    editorial = models.ForeignKey(Editorial, on_delete=models.CASCADE)