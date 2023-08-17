from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.urls import reverse_lazy
from GestorIP.models import *
from GestorIP.forms import *

from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DetailView
from django.views.generic import DeleteView
from django.views.generic import TemplateView

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    return render(request, "GestorIP/index.html", {"mensaje":"Sistema de gestión de activos.", "mensaje2":"Estimado tutor, regístrese, o proceda a loguearse, si ya lo hizo."})

def register(request):
    if request.method == 'POST':
        form = RegistroUsuariosForm(request.POST) # UserCreationForm 
        if form.is_valid():  # Si pasó la validación de Django
            user = form.save()  # Guarda el usuario
            avatar = Avatar(user=user, imagen=form.cleaned_data['imagen'])
            avatar.save()
            return render(request, "GestorIP/regexitoso.html", {"mensaje":"Su usuario fue creado exitosamente."})        
    else:
        form = RegistroUsuariosForm() # UserCreationForm 

    return render(request, "GestorIP/registrarse.html", {"form": form})   

def login_request(request):
    if request.method == "POST":
        miForm = AuthenticationForm(request, data=request.POST)
        if miForm.is_valid():
            usuario = miForm.cleaned_data.get('username')
            clave = miForm.cleaned_data.get('password')
            user = authenticate(username=usuario, password=clave)
            if user is not None:
                login(request, user)

                return render(request, "GestorIP/loginexitoso.html", {"mensaje":f"Bienvenido al sistema {usuario}"})

            else:
                return render(request, "GestorIP/login.html", {"form":miForm, "mensaje": "Datos Inválidos"})
        else:    
            return render(request, "GestorIP/login.html", {"form":miForm, "mensaje": "Datos Inválidos"})

    miForm = AuthenticationForm()

    return render(request, "GestorIP/login.html", {"form":miForm, "mensaje": "Ingrese sus credenciales de acceso."})    

def desloguearse(request):
    logout(request)
    return render(request, "GestorIP/index.html", {"mensaje":"Te has deslogueado exitosamente."})

@login_required
def editarPerfil(request):
    usuario = request.user
    if request.method == "POST":
        form = UserEditForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return render(request, "GestorIP/loginexitoso.html", {'mensaje': f"Usuario {usuario.username} actualizado correctamente."})
        else:
            return render(request, "GestorIP/perfil.html", {'form': form, 'mensaje':"Edite sus datos."})
    else:
        form = UserEditForm(instance=usuario)
    return render(request, "GestorIP/perfil.html", {'form': form, 'usuario':usuario.username, 'mensaje':"Edite sus datos."})

@login_required
def quiensoy(request):
    return render(request, "GestorIP/quiensoy.html")

@login_required
def menumarcas(request):
    return render(request, "GestorIP/marcas_menu.html")

@login_required
def menumdi(request):
    return render(request, "GestorIP/mdi_menu.html")

@login_required
def menupmu(request):
    return render(request, "GestorIP/pmu_menu.html")

@login_required
def menuoys(request):
    return render(request, "GestorIP/oys_menu.html")

# Views para Marcas.

class creacionMarcas(LoginRequiredMixin, CreateView):
    model = marcas
    fields = ['tipo', 'denominacion', 'fechapresentacion', 'fechaotorgamiento']
    template_name = 'GestorIP/marcas_form.html'
    success_url = reverse_lazy('creacionMarcaExitosa')

class creacionMarcaExitosa(LoginRequiredMixin, TemplateView):
    template_name = "GestorIP/marcas_creacionexitosa.html"
    
class listarMarcas(LoginRequiredMixin, ListView):
    model = marcas
    template_name = "GestorIP/marcas_list.html"

class marcasDetailView(LoginRequiredMixin, DetailView):
    model = marcas
    template_name = "GestorIP/marcas_detail.html"

class marcasUpdateView(LoginRequiredMixin, UpdateView):
    model = marcas
    fields = ['tipo', 'denominacion', 'fechapresentacion', 'fechaotorgamiento']
    success_url = reverse_lazy('creacionMarcaExitosa')

class marcasDeleteView(LoginRequiredMixin, DeleteView):
    model = marcas
    success_url = reverse_lazy('listarmarcas')

# Views para Modelos y Diseños Industriales.

class creacionMDindustriales(LoginRequiredMixin, CreateView):
    model = mdindustriales
    fields = ['tipo', 'denominacion', 'fechapresentacion', 'fechaotorgamiento']
    template_name = 'GestorIP/mdindustriales_form.html'
    success_url = reverse_lazy('creacionMDexitosa')
    
class creacionMDexitosa(TemplateView):
    template_name = "GestorIP/md_creacionexitosa.html"

class mdiListView(LoginRequiredMixin, ListView):
    model = mdindustriales
    template_name = "GestorIP/mdi_list.html"

class mdiDetailView(LoginRequiredMixin, DetailView):
    model = mdindustriales
    template_name = "GestorIP/mdi_detail.html"

class mdiUpdateView(LoginRequiredMixin, UpdateView):
    model = mdindustriales
    fields = ['tipo', 'denominacion', 'fechapresentacion', 'fechaotorgamiento']
    success_url = reverse_lazy('creacionMDexitosa')

class mdiDeleteView(LoginRequiredMixin, DeleteView):
    model = mdindustriales
    success_url = reverse_lazy('listarmdi')

# Views para Patentes y Modelos de Utilidad.

class creacionPMU(LoginRequiredMixin, CreateView):
    model = pmu
    fields = ['tipo', 'denominacion', 'fechapresentacion', 'fechaotorgamiento']
    template_name = 'GestorIP/pmu_form.html'
    success_url = reverse_lazy('creacionPMUexitosa')
    
class creacionPMUexitosa(TemplateView):
    template_name = "GestorIP/pmu_creacionexitosa.html"
    
class pmuListView(LoginRequiredMixin, ListView):
    model = pmu
    template_name = "GestorIP/pmu_list.html"

class pmuDetailView(LoginRequiredMixin, DetailView):
    model = pmu
    template_name = "GestorIP/pmu_detail.html"

class pmuUpdateView(LoginRequiredMixin, UpdateView):
    model = pmu
    fields = ['tipo', 'denominacion', 'fechapresentacion', 'fechaotorgamiento']
    success_url = reverse_lazy('creacionPMUexitosa')

class pmuDeleteView(LoginRequiredMixin, DeleteView):
    model = pmu
    success_url = reverse_lazy('listarpmu')
    
# Views para obras y software.

class creacionOYS(LoginRequiredMixin, CreateView):
    model = obrasysoftware
    fields = ['tipo', 'denominacion', 'fechadeposito', 'fechaconstancia']
    template_name = 'GestorIP/obrasysoftware_form.html'
    success_url = reverse_lazy('creacionOYSexitosa')
    
class creacionOYSexitosa(TemplateView):
    template_name = "GestorIP/OYS_creacionexitosa.html"

class oysListView(LoginRequiredMixin, ListView):
    model = obrasysoftware
    template_name = "GestorIP/obrasysoftware_list.html"

class oysDetailView(LoginRequiredMixin, DetailView):
    model = obrasysoftware
    template_name = "GestorIP/obrasysoftware_detail.html"

class oysUpdateView(LoginRequiredMixin, UpdateView):
    model = obrasysoftware
    fields = ['tipo', 'denominacion', 'fechadeposito', 'fechaconstancia']
    success_url = reverse_lazy('creacionOYSexitosa')

class oysDeleteView(LoginRequiredMixin, DeleteView):
    model = obrasysoftware
    success_url = reverse_lazy('listaroys')
    
# View para agregar avatar.

@login_required
def agregarAvatar(request):
    if request.method == "POST":
        form = AvatarFormulario(request.POST, request.FILES)
        if form.is_valid():
            u = request.user
            avatar_viejo = Avatar.objects.filter(user=u).first()
            if avatar_viejo:
                avatar_viejo.delete()

            avatar_nuevo = Avatar(user=u, imagen=form.cleaned_data['imagen'])
            avatar_nuevo.save()

            request.session['avatar'] = avatar_nuevo.imagen.url

            return render(request, "GestorIP/index.html")
    else:
        form = AvatarFormulario()
    
    return render(request, "GestorIP/agregarAvatar.html", {'form': form})

# Views para busqueda. 

@login_required
def buscador(request):
    return render(request, "GestorIP/Busqueda_inicio.html")

@login_required
def buscar2(request):
    if 'denominacion' in request.GET:
        denominacion = request.GET['denominacion']
        modelos = [marcas, mdindustriales, pmu, obrasysoftware]
        resultados = {}

        for modelo in modelos:
            nombre_modelo = modelo.__name__
            resultados[nombre_modelo] = modelo.objects.filter(denominacion__icontains=denominacion)
        
        return render(request, "GestorIP/Busqueda_resultados.html", {'resultados': resultados})
    return render(request, "GestorIP/Busqueda_resultados.html")




    