from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.db.models.signals import pre_save
from Uniamiga.utils import unique_slug_generator
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

    def __str__(self):
        return self.Nombre

class Inscripcion(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Inscripcion')
    Cursos = models.ForeignKey(Cursos, on_delete=models.CASCADE,related_name='Inscripcion')



#class grupo_familiar(models.Model):
#    parentesco=models.CharField(max_length=50,null=False,blank=False)
#    pacientes=models.ForeignKey(pacientes,on_delete=models.CASCADE)
#    medico=models.ForeignKey(medico,on_delete=models.CASCADE)

class Archivo(models.Model):
    Curso = models.ForeignKey(Cursos, on_delete=models.CASCADE, related_name='Cursos')
    Nombre=models.CharField(max_length=150,null=False,blank=False)
    Descripcion=models.TextField(max_length=150,null=False,blank=False)
    Media=models.FileField(upload_to='myfolder/',blank=True,null=True)
    slug=models.SlugField(max_length=200,null=True,blank=True)

def slug_generator(sender,instance,*args,**Kwargs):
    if not instance.slug:
        instance.slug=unique_slug_generator(instance)
pre_save.connect(slug_generator,sender=Archivo)