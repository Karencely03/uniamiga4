#Django
from django.urls import path

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
    path('Cursos/eliminar/<int:pk>',Eliminar_Cursos.as_view(),name='eliminar_curso')
]