from django.urls import path, include
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', index, name="inicio"),
    path('register/', register, name="register"),
    path('login/', login_request, name="login"),
    path('logout/', desloguearse, name="logout"),
    path('editarPerfil/', editarPerfil, name="editarPerfil"),
    path('agregar_avatar/', agregarAvatar, name="agregar_avatar"),

    path('buscador/', buscador, name="buscador"),
    path('buscar2/', buscar2, name="buscar2"),
    
    path('quiensoy/', quiensoy, name="quiensoy"),
    
    path('menumarcas/', menumarcas, name='menumarcas'),
    path('crearmarca/', creacionMarcas.as_view(), name="crearmarca"),
    path('creacionMarcaExitosa/', creacionMarcaExitosa.as_view(), name='creacionMarcaExitosa'),   
    path('listarmarcas/',listarMarcas.as_view(), name='listarmarcas'),
    path('detail_marcas/<int:pk>/', marcasDetailView.as_view(), name='detail_marcas'),
    path('update_marcas/<int:pk>/', marcasUpdateView.as_view(), name='update_marcas'),
    path('marcaBorrada/<int:pk>', marcasDeleteView.as_view(), name='delete_marcas'),

    path('menumdi/', menumdi, name='menumdi'),
    path('crearMD/', creacionMDindustriales.as_view(), name="crearMD"),
    path('creacionMDExitosa/', creacionMDexitosa.as_view(), name='creacionMDexitosa'),
    path('listarMDI/', mdiListView.as_view(), name='listarmdi'),
    path('detail_mdi/<int:pk>/', mdiDetailView.as_view(), name='detail_mdi'),
    path('update_mdi/<int:pk>', mdiUpdateView.as_view(), name='update_mdi'),
    path('delete_mdi/<int:pk>/', mdiDeleteView.as_view(), name='delete_mdi'),
    
    path('menupmu/', menupmu, name='menupmu'),
    path('crearPMU/', creacionPMU.as_view(), name="crearPMU"),
    path('creacionPMUExitosa/', creacionPMUexitosa.as_view(), name='creacionPMUexitosa'),
    path('listarPMU/', pmuListView.as_view(), name='listarpmu'),
    path('detail_pmu/<int:pk>/', pmuDetailView.as_view(), name='detail_pmu'), 
    path('update_pmu/<int:pk>', pmuUpdateView.as_view(), name='update_pmu'),    
    path('delete_pmu/<int:pk>/', pmuDeleteView.as_view(), name='delete_pmu'),

    path('menuoys/', menuoys, name='menuoys'),
    path('crearOYS/', creacionOYS.as_view(), name="crearOYS"),
    path('creacionOYSExitosa/', creacionOYSexitosa.as_view(), name='creacionOYSexitosa'),
    path('listarOYS/', oysListView.as_view(), name='listaroys'),
    path('detail_oys/<int:pk>/', oysDetailView.as_view(), name='detail_oys'),
    path('update_oys/<int:pk>', oysUpdateView.as_view(), name='update_oys'), 
    path('delete_oys/<int:pk>/', oysDeleteView.as_view(), name='delete_oys'),       
]