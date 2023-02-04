from django.urls import path

from AppHospitalV import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
   
    path('', views.inicio, name="Inicio"), 
    path('especialidades', views.especialidades, name="Especialidades"),
    path('staff', views.staff, name="Staff"),
    path('laboratorio', views.laboratorio, name="Laboratorio"),
    path('imagenes', views.imagenes, name="EstudiosDeImagen"),
    path('especialidadesform', views.especialidadesform, name="EspecialidadesFormulario"),
    path('profesion', views.profesion, name="Profesion"),
    path('busquedaProfesion', views.busquedaProfesion, name="BusquedaProfesion"),
    path('buscar/', views.buscar),
    path('leerProfesionales', views.leerProfesionales, name="LeerProfesionales"),
    path('resultadoBusqueda', views.buscar, name="ResultadoBusqueda"),
    path('especialidades/list', views.EspecialidadesList.as_view(), name='List'),
    path(r'^(?P<pk>\d+)$', views.EspecialidadesDetalle.as_view(), name='Detail'),
    path(r'^nuevo$', views.EspecialidadesCreacion.as_view(), name='New'),
    path(r'^editar/(?P<pk>\d+)$', views.EspecialidadesUpdate.as_view(), name='Edit'),
    path(r'^borrar/(?P<pk>\d+)$', views.EspecialidadesDelete.as_view(), name='Delete'),
    path('login', views.login_request, name="Login"),
    path('register', views.register, name='Register'),
    path('logout', LogoutView.as_view(template_name='AppHospitalV/logout.html'), name='Logout'),
    path('editarPerfil', views.editarPerfil, name="EditarPerfil"), 
    path ('Nosotros', views.Nosotros, name="Nosotros")

]