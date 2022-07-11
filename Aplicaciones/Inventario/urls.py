from django.urls import path
from .  import views


urlpatterns=[
    #Regritar las tablas
    path('registrarEntradas/', views.registrarEntradas),
    path('registrarHome/',views.registrarHome),
    path('registrarTeclado/',views.registrarTeclados),
    path('registrarMonitor/', views.registrarMonitor),
    path('registrarComputador/',views.registrarCompu),
    
    #Pagina para entrar la edicion 
    path('edicionEntradas/<codigo>', views.edicionEntradas),
    path('home/edicionEntradas/<codigo>',views.edicionHome),
    path('edicionTeclados/<codigo>',views.edicionTeclado),
    path('edicionC/<codigo>', views.edicionMonitor),
    path('edicionComputador/<codigo>',views.edicionCompu),

    #Para editar como tal la atabla
    path('editarCurso/',views.editarCurso),
    path('editarH/',views.editarH),
    path('editarT/',views.editarT),
    path('editarM/',views.editarM),
    path('editarC/',views.editarC),
    #
    # Eliminar 
    path('eliminacionEntradas/<codigo>', views.eliminacionEntradas),
    path('home/eliminacionEntradas/<codigo>',views.eliminarHome),
    path('eliminarT/<codigo>',views.eliminarTeclado),
    path('eliminarM/<codigo>',views.eliminarMonitor),
    path('eliminarC/<codigo>',views.eliminarComputador),
    
    #Para navergar en cada tablas
    path('', views.home),
    #path('salir/',views.salir, name='salir'), 
    path('home/', views.Inicio),
    path('teclado/', views.Teclados),
    path('monitor/', views.Monitores),
    path('computador/', views.Computadores),

    path('registro/',views.registro, name='registro'),

    #Usuario
    path('usuario/', views.usuarios)

]