#django

from django.shortcuts import render, redirect
from django.views.generic import CreateView,ListView,UpdateView,DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate
from django.contrib.auth import login

#Forms
from .forms import *

#Models
from .models import *


def user_create(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user = authenticate(username=request.POST.get('username'), password=request.POST.get('password1'))
            if user:
                login(request, user)
                if request.POST.get('tipo_usuario') == 'M':
                    return redirect('medico_create', id=user.id)
                else:
                    return redirect('paciente_create', id=user.id)
    else:
        form = UserCreationForm()

    return render(request, 'appconsultaeps/user_form.html', {'form': form})
    

def paciente_create(request, id):
    user = User.objects.get(pk=id)

    if request.method == 'POST':
        #edad = request.POST.get('edad')
        #peso = request.POST.get('peso')
        #estatura = request.POST.get('estatura')
        #estado_civil = request.POST.get('estado_civil')
        #doc = tipo_doc.objects.get(pk=request.POST.get('tipo_doc'))
        estudiante = estudiantes.objects.create(user=user)


        if estudiantes:

            return redirect('home')

    return render(request, 'appconsultaeps/user_form.html', {'form': PacienteForm})


def medico_create(request, id):
    user = User.objects.get(pk=id)
    if request.method == 'POST':
        #doc = tipo_doc.objects.get(pk=request.POST.get('tipo_doc'))
        #Numero_doc = request.POST.get('Numero_doc')
        #telefono = request.POST.get('telefono')
        #especialist = especialista.objects.get(pk=request.POST.get('especialista'))
        
        medico_create = Tutor.objects.create(user=user)
        if medico_create:
            return redirect('home')
    return render(request, 'appconsultaeps/user_form.html', {'form': MedicoForm})

class Crear_Curso(CreateView):
    model = Cursos
    form_class = CursosForm
    template_name = 'Cursos.html'
    success_url = reverse_lazy('listar_curso')
    success_message = 'Curso creado exitosamente!'

def inscripcion_create(request,id):
    user = User.objects.get(pk=id)

    if request.method=='POST':
        Curso=Cursos.objects.get(pk=request.POST.get('Cursos'))
        inscripcion_create=Inscripcion.objects.create(user=user,Cursos=Curso)
        if inscripcion_create:
            return redirect('home')
    return render(request,'UniamigaApp/inscripcion_form.html',{'form':IncripcionForm})

class Listar_Inscritos(ListView):

    model = Inscripcion
    form_class=IncripcionForm
    template_name = 'UniamigaApp/inscripcion_list.html'

class Crear_Inscripcion(CreateView):
    model = Inscripcion
    form_class = IncripcionForm
    
    success_url = reverse_lazy('home')


class Listar_Curso(ListView):
    model = Cursos
    form_class=CursosForm
    template_name = 'listar_cursos.html'

class Listar_Cursos(ListView):
    model = Cursos
    form_class=CursosForm
    template_name = 'lista.html'


class Actualizar_Cursos(UpdateView):
    model = Cursos
    template_name = 'cursos.html'
    form_class = CursosForm
    success_url = reverse_lazy('listar_curso')

class Eliminar_Inscritos(DeleteView):
    model = Inscripcion
    success_url = reverse_lazy('home')

class Eliminar_Cursos(DeleteView):
    model = Cursos
    success_url = reverse_lazy('listar_curso')




def Subir_Archivo(request,id):
    Ocursos=Cursos.objects.get(id=id)
    titulo = "Bienvenidos"
    form = RegistradoForm(request.POST or None,request.FILES or None)

    context = {
        "titulo": titulo,
        "form":form
    }

    if form.is_valid():
        instance=form.save(commit=False)

        Nombre=form.cleaned_data.get("Nombre")
        Descripcion=form.cleaned_data.get("Descripcion")
        Curso=Ocursos
        form.save()



    return render(request,'Archivos.html',context)


def mostrarArchivos(request):
    Archivos = Archivo.objects.all()
    context = {"Archivos": Archivos}
    return render(request,"ListarAr.html",context)

def tareas(request):
    Archivos= Archivo.objects.all()
    context ={"Archivos":Archivos}
    return render(request ,"Tareas.html",context)

