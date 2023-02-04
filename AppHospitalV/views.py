from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from AppHospitalV.models import Staff, Especialidades, Avatar


def inicio(request):

      return render(request, "AppHospitalV/inicio.html")

def especialidades(request):

      return render(request, "AppHospitalV/especialidades.html")

def staff(request):

      return render(request, "AppHospitalV/staff.html")

def laboratorio(request):

      return render(request, "AppHospitalV/laboratorio.html")

def imagenes(request):

      return render(request, "AppHospitalV/imagenes.html")

def Nosotros(request):

      return render(request, "AppHospitalV/Nosotros.html")



from AppHospitalV.forms import EspecialidadesFormulario, StaffFormulario, UserRegisterForm, UserEditForm

def especialidadesform(request):

      if request.method == "POST":
         
          miFormulario = EspecialidadesFormulario(request.POST) 
          print(miFormulario)
 
          if miFormulario.is_valid:
                 informacion = miFormulario.cleaned_data
                 especialidad = Especialidades (nombre=informacion["especialidad"], adulto=informacion["adulto"], pediatrico=informacion["pediatrico"])
                 especialidad.save()
                 return render(request, "AppHospitalV/inicio.html")
      else:
          miFormulario = EspecialidadesFormulario()
    
      return render(request, "AppHospitalV/especialidadesform.html", {"miFormulario": miFormulario})

def profesion(request):

      if request.method == "POST":

            miFormulario = StaffFormulario(request.POST) 
            print(miFormulario)
 
            if miFormulario.is_valid:
                 informacion = miFormulario.cleaned_data
                 
                 staff = Staff(nombre=informacion["nombre"], apellido=informacion["apellido"],
                 email=informacion['email'], profesion=informacion['profesion'])
                 staff.save()

                 return render(request, "AppHospitalV/inicio.html")
      else:
           miFormulario = StaffFormulario()
    
      return render(request, "AppHospitalV/profesion.html", {"miFormulario": miFormulario})


def busquedaProfesion(request):
      
      return render(request, "AppHospitalV/busquedaProfesion.html")

def buscar(request):

   if request.GET["profesion"]:

      profesion = request.GET['profesion']
      staff = Staff.objects.filter(profesion__icontains=profesion)
      
      return render(request, "AppHospitalV/resultadoBusqueda.html", {"staff":staff, "profesion":profesion})

   else:

      respuesta = "No existen datos"

   return HttpResponse(respuesta)



def leerProfesionales(request):
        staff = Staff.objects.all() 
        contexto= {"staff":staff}
        return render(request, "AppHospitalV/leerProfesionales.html",contexto)


from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


class EspecialidadesList(ListView):

      model  = Especialidades
      template_name = "AppHospitalV/especialidades_list.html"

class EspecialidadesDetalle(DetailView):

      model = Especialidades
      template_name = "AppHospitalV/especialidades_detalle.html"


class EspecialidadesCreacion(CreateView):

      model = Especialidades
      success_url = "/AppHospitalV/especialidades/list"
      fields = ['especialidad', 'adulto', 'pediatrico']


class EspecialidadesUpdate(UpdateView):

      model = Especialidades
      success_url = "/AppHospitalV/especialidades/list"
      fields = ['especialidad', 'adulto', 'pediatrico']


class EspecialidadesDelete(DeleteView):

      model = Especialidades
      success_url = "/AppHospitalV/especialidades/list"


from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate

def login_request(request):

    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid(): 

            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')

            user = authenticate(username= usuario, password=contrasenia)

            if user is not None:
               avatar = Avatar.objects.filter(user=user)[0].imagen.url
               login(request, user)

               return render(request, "AppHospitalV/inicio.html", {"mensaje":f"Bienvenido/a {usuario}", "avatar":avatar})
            else:
               return render(request, "AppHospitalV/inicio.html", {"mensaje":"Datos incorrectos"})
           
        else:

            return render(request, "AppHospitalV/inicio.html", {"mensaje":"Formulario erroneo"})

    form = AuthenticationForm()

    return render(request, "AppHospitalV/login.html", {"form": form})


from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


def register(request):

      if request.method == 'POST':

            form = UserRegisterForm(request.POST)
            if form.is_valid():

                  username = form.cleaned_data['username']
                  form.save()
                  return render(request,"AppHospitalV/inicio.html" ,  {"mensaje":"Usuario Creado Exitosamente"})

      else:       
            form = UserRegisterForm()     

      return render(request,"AppHospitalV/registro.html" ,  {"form":form})


from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


@login_required
def inicio(request):

      return render(request, "AppHospitalV/inicio.html")

@login_required
def editarPerfil(request):

    usuario = request.user

    if request.method == 'POST':

        miFormulario = UserEditForm(request.POST)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password2']
            usuario.last_name = informacion['last_name']
            usuario.first_name = informacion['first_name']

            usuario.save()

            return render(request, "AppHospitalV/inicio.html")

    else:

        miFormulario = UserEditForm(initial={'email': usuario.email})

    return render(request, "AppHospitalV/editarPerfil.html", {"miFormulario": miFormulario, "usuario": usuario})





