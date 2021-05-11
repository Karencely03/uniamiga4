#Django
from django.urls import path,re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
#Views
from .views import *

urlpatterns = [
    path('usuario/create', user_create, name='usuario_create'),
    path('paciente/create/<int:id>', paciente_create, name='paciente_create'),
    path('medico/create/<int:id>', medico_create, name='medico_create'),
    path('Cursos/create',Crear_Curso.as_view(),name='crear_curso'),
    path('Cursos/list',Listar_Curso.as_view(),name='listar_curso'),
    path('Cursos/Listar',Listar_Cursos.as_view(),name='Listar_cursos'),
    path('Cursos/editar/<int:pk>',Actualizar_Cursos.as_view(),name='editar_curso'),
    path('Cursos/eliminar/<int:pk>',Eliminar_Cursos.as_view(),name='eliminar_curso'),
    path('Inscripcioncreate/<int:id>',Crear_Inscripcion.as_view(),name='Crear_Inscripcion'),
    path('Inscribir/cursos/<int:id>',inscripcion_create,name='cursos_create'),
    path('Inscribir/Listar/<int:id>',Listar_Inscritos.as_view(),name='Listar_Inscritos'),
    path('Inscribir/eliminar/<int:pk>',Eliminar_Inscritos.as_view(),name='eliminar_Inscripcion'),
    path('Archivo',Subir_Archivo,name='Archivo_create'),
    path('Tareas',tareas,name='Tareas'),
    path('Mostrar',mostrarArchivos,name='mostra_archivo')
]


urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)