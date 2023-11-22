from django.urls import path
from . import views

urlpatterns = [
    
    # URLs Pagina de inicio-------------------------------------------------------------------
    # path('Nombre de la vista osea el url que llama', 'nombre en el archivo views', 'nombre no se de que xD')
    path('', views.pagina_inicio, name='pagina_inicio'),
    path('acerca_de_mi/', views.acerca_de_mi, name='acerca_de_mi'),
    
    # URLs para comunidad-------------------------------------------------------------------------
    
    path('subpaginas/Comunidades/inicio_comunidad', views.inicio_comunidad, name='inicio comunidad'),
    #     templates/subpaginas/Comunidades/inicio_comunidad.html
    
    path('templates/subpaginas/comunidades/crear_comunidad/', views.crear_comunidad, name='crear_comunidad'),
    path('templates/subpaginas/comunidades/listar_comunidades/', views.listar_comunidades, name='listar_comunidades'),
    path('templates/subpaginas/comunidades/editar_comunidad/', views.editar_comunidad, name='editar_comunidad'),
    path('templates/subpaginas/comunidades/eliminar_comunidad/', views.eliminar_comunidad, name='eliminar_comunidad'),
    path('templates/subpaginas/comunidades/ver_comunidad/', views.ver_comunidad, name='ver_comunidad'),
    
    # URLs para usuario---------------------------------------------------------------------------
    path('inicio_usuario/', views.inicio_usuario, name='inicio_usuario'),
    path('crear_usuario/', views.crear_usuario, name='crear_usuario'),
    path('listar_usuarios/', views.listar_usuarios, name='listar_usuarios'),
    path('editar_usuario/', views.editar_usuario, name='editar_usuario'),
    path('eliminar_usuario/', views.eliminar_usuario, name='eliminar_usuario'),
    path('ver_usuario/', views.ver_usuario, name='ver_usuario'),
    
    
    # URLs para administrador-----------------------------------------------------------------------
    path('inicio_administrador/', views.inicio_administrador, name='inicio_administrador'),
    path('crear_administrador/', views.crear_administrador, name='crear_administrador'),
    path('listar_administradores/', views.listar_administradores, name='listar_administradores'),
    path('editar_administrador/', views.editar_administrador, name='editar_administrador'),
    path('eliminar_administrador/', views.eliminar_administrador, name='eliminar_administrador'),
    
    
    # URLs para propietario---------------------------------------------------------------------------------
    path('inicio_propietario/', views.inicio_propietario, name='inicio_propietario'),
    path('crear_propietario/', views.crear_propietario, name='crear_propietario'),
    path('listar_propietarios/', views.listar_propietarios, name='listar_propietarios'),
    path('editar_propietario/', views.editar_propietario, name='editar_propietario'),
    path('eliminar_propietario/', views.eliminar_propietario, name='eliminar_propietario'),
    path('ver_propietario/', views.ver_propietario, name='ver_propietario'),
    
    
    # URLs para visita---------------------------------------------------------------------------------
    path('inicio_visita/', views.inicio_visita, name='inicio_visita'),
    path('crear_visita/', views.crear_visita, name='crear_visita'),
    path('listar_visitas/', views.listar_visitas, name='listar_visitas'),
    path('editar_visita/', views.editar_visita, name='editar_visita'),
    path('eliminar_visita/', views.eliminar_visita, name='eliminar_visita'),
    path('ver_visita/', views.ver_visita, name='ver_visita'),

    
    ]