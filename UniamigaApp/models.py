from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator


#class tipo_doc (models.Model):
 #   doc=models.CharField(max_length=20, null=False,blank=False)


class estudiantes(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='estudiantes')
    #edad=models.PositiveIntegerField()
    #peso=models.PositiveIntegerField()
    #estatura=models.PositiveIntegerField()
    #estado_civil=models.CharField(max_length=45, null=False,blank=False)
    #tipo_doc=models.ForeignKey(tipo_doc, on_delete=models.CASCADE)
    



class especialista(models.Model):
    especialidad=models.CharField(max_length=50,null=False,blank=False)


class Tutor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='Tutor')
    #Numero_doc=models.IntegerField(unique=True, validators=[MinValueValidator(1)])
    #telefono=models.PositiveIntegerField()
    #tipo_doc = models.ForeignKey(tipo_doc, on_delete=models.CASCADE)
    #especialista=models.ForeignKey(especialista,on_delete=models.CASCADE)


class Cursos(models.Model):

    Nombre=models.CharField(max_length=50,null=True,blank=True)
    Descripcion=models.TextField(max_length=150,null=False,blank=False)


class Inscripcion(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='Inscripcion')
    Cursos = models.OneToOneField(Cursos, on_delete=models.CASCADE,related_name='Inscripcion')




#class grupo_familiar(models.Model):
#    parentesco=models.CharField(max_length=50,null=False,blank=False)
#    pacientes=models.ForeignKey(pacientes,on_delete=models.CASCADE)
#    medico=models.ForeignKey(medico,on_delete=models.CASCADE)