from django.shortcuts import render, redirect, get_object_or_404
from .models import Comunidad, Propietario, Administrador, Usuario, Visita
from .forms import ComunidadForm, PropietarioForm, AdministradorForm, UsuarioForm, VisitaForm
from django.http import HttpResponse





#Pagina de Inicio***************************************************************************************************************************)1
def pagina_inicio(request):
    return render(request, 'pagina_inicio.html')

def acerca_de_mi(request):
    return render(request), 'acerca_de_mi.html'


#Vista para comunidad***************************************************************************************************************************)2

def inicio_comunidad(request):
    # Esta función simplemente renderiza la página de inicio de la comunidad
    return render(request, 'visitApp/templates/subpaginas/Comunidades/inicio_comunidad.html')

#----------------------------------------------------------------------------------------------------->

def listar_comunidades(request):
    comunidad = Comunidad.objects.all()
    return render(request, 'templates/subpaginas/Comunidades/listar_comunidad.html', {'comunidad': comunidad})

#----------------------------------------------------------------------------------------------------->

def ver_comunidad(request, pk):
    # Recupera la comunidad específica usando su clave primaria (pk)
    comunidad = get_object_or_404(Comunidad, pk=pk)
    return render(request, 'templates/subpaginas/Comunidades/ver_comunidad.html', {'comunidad': comunidad})

#----------------------------------------------------------------------------------------------------->

def crear_comunidad(request):
    if request.method == 'POST':
        # Si la solicitud es POST, procesa el formulario
        form = ComunidadForm(request.POST, request.FILES)
        if form.is_valid():
            # Si el formulario es válido, guarda la nueva comunidad en la base de datos
            comunidad = form.save()
            return redirect('templates/subpaginas/Comunidades/ver_comunidad', pk=comunidad.pk)
    else:
        # Si la solicitud no es POST, muestra un formulario en blanco para crear una nueva comunidad
        form = ComunidadForm()
    return render(request, 'templates/subpaginas/Comunidades/crear_comunidad.html', {'form': form})

#----------------------------------------------------------------------------------------------------->

def editar_comunidad(request, pk):
    # Recupera la comunidad específica usando su clave primaria (pk)
    comunidad = get_object_or_404(Comunidad, pk=pk)
    if request.method == 'POST':
        # Si la solicitud es POST, procesa el formulario de edición
        form = ComunidadForm(request.POST, request.FILES, instance=comunidad)
        if form.is_valid():
            # Si el formulario es válido, guarda los cambios en la comunidad
            comunidad = form.save()
            return redirect('templates/subpaginas/Comunidades/ver_comunidad', pk=comunidad.pk)
    else:
        # Si la solicitud no es POST, muestra el formulario de edición con los datos actuales de la comunidad
        form = ComunidadForm(instance=comunidad)
    return render(request, 'templates/subpaginas/Comunidades/editar_comunidad.html', {'form': form, 'comunidad': comunidad})

#----------------------------------------------------------------------------------------------------->

def eliminar_comunidad(request, pk):
    # Recupera la comunidad específica usando su clave primaria (pk)
    comunidad = get_object_or_404(Comunidad, pk=pk)
    comunidad.delete()
    return redirect('templates/subpaginas/Comunidades/listar_comunidades')

# Vista para propietario***************************************************************************************************************************)3

def listar_propietarios(request):
    propietario = Propietario.objects.all()
    return render(request, 'listar_propietarios.html', {'propietario': propietario})

#-----------------------------------------------------------------------------------------------------

def ver_propietario(request, pk):
    # Recupera la propietario específica usando su clave primaria (pk)
    propietario = get_object_or_404(Propietario, pk=pk)
    return render(request, 'ver_propietario.html', {'propietario': propietario})

#-----------------------------------------------------------------------------------------------------

def crear_propietario(request):
    if request.method == 'POST':
        # Si la solicitud es POST, procesa el formulario
        form = PropietarioForm(request.POST, request.FILES)
        if form.is_valid():
            # Si el formulario es válido, guarda la nueva propietario en la base de datos
            propietario = form.save()
            return redirect('ver_propietario', pk=propietario.pk)
    else:
        # Si la solicitud no es POST, muestra un formulario en blanco para crear una nueva propietario
        form = PropietarioForm()
    return render(request, 'crear_propietario.html', {'form': form})

#-----------------------------------------------------------------------------------------------------


def editar_propietario(request, pk):
    
    
    # Recupera la propietario específica usando su clave primaria (pk)
    propietario = get_object_or_404(Propietario, pk=pk)
    if request.method == 'POST':
        # Si la solicitud es POST, procesa el formulario de edición
        form = PropietarioForm(request.POST, request.FILES, instance=propietario)
        if form.is_valid():
            # Si el formulario es válido, guarda los cambios en la propietario
            propietario = form.save()
            return redirect('ver_propietario', pk=propietario.pk)
    else:
        # Si la solicitud no es POST, muestra el formulario de edición con los datos actuales de la propietario
        form = PropietarioForm(instance=propietario)
    return render(request, 'editar_propietario.html', {'form': form, 'propietario': propietario})

#-----------------------------------------------------------------------------------------------------

def eliminar_propietario(request, pk):
    # Recupera la propietario específica usando su clave primaria (pk)
    propietario = get_object_or_404(Propietario, pk=pk)
    propietario.delete()
    return redirect('listar_propietarios')



#----------------------------------------------------------------------------------------------------->6

def inicio_propietario(request):
    # Esta función simplemente renderiza la página de inicio de la comunidad
    return render(request, 'inicio_propietario')


# Vista para usuario***************************************************************************************************************************)4
def listar_usuarios(request):
    usuario = Usuario.objects.all()
    return render(request, 'listar_usuarios.html', {'usuario': usuario})

#-----------------------------------------------------------------------------------------------------

def ver_usuario(request, pk):
    # Recupera la usuario específica usando su clave primaria (pk)
    usuario = get_object_or_404(Usuario, pk=pk)
    return render(request, 'ver_usuario.html', {'usuario': usuario})

#-----------------------------------------------------------------------------------------------------

def crear_usuario(request):
    if request.method == 'POST':
        # Si la solicitud es POST, procesa el formulario
        form = UsuarioForm(request.POST, request.FILES)
        if form.is_valid():
            # Si el formulario es válido, guarda la nueva usuario en la base de datos
            usuario = form.save()
            return redirect('ver_usuario', pk=usuario.pk)
    else:
        # Si la solicitud no es POST, muestra un formulario en blanco para crear una nueva usuario
        form = UsuarioForm()
    return render(request, 'crear_usuario.html', {'form': form})

#-----------------------------------------------------------------------------------------------------

def editar_usuario(request, pk):
    # Recupera la usuario específica usando su clave primaria (pk)
    usuario = get_object_or_404(Usuario, pk=pk)
    if request.method == 'POST':
        # Si la solicitud es POST, procesa el formulario de edición
        form = UsuarioForm(request.POST, request.FILES, instance=usuario)
        if form.is_valid():
            # Si el formulario es válido, guarda los cambios en la usuario
            usuario = form.save()
            return redirect('ver_usuario', pk=usuario.pk)
    else:
        # Si la solicitud no es POST, muestra el formulario de edición con los datos actuales de la usuario
        form = UsuarioForm(instance=usuario)
    return render(request, 'editar_usuario.html', {'form': form, 'usuario': usuario})

#-----------------------------------------------------------------------------------------------------

def eliminar_usuario(request, pk):
    # Recupera la usuario específica usando su clave primaria (pk)
    usuario = get_object_or_404(Usuario, pk=pk)
    usuario.delete()
    return redirect('listar_usuarios')

#----------------------------------------------------------------------------------------------------->6

def inicio_usuario(request):
    # Esta función simplemente renderiza la página de inicio de la comunidad
    return render(request, 'inicio_usuario')

# Visita para administrador***************************************************************************************************************************)5

def listar_administradores(request):
    administrador = Administrador.objects.all()
    return render(request, 'listar_administradores.html', {'administrador': administrador})

#-----------------------------------------------------------------------------------------------------

def ver_administrador(request, pk):
    # Recupera la administrador específica usando su clave primaria (pk)
    administrador = get_object_or_404(Administrador, pk=pk)
    return render(request, 'ver_administrador.html', {'administrador': administrador})

#-----------------------------------------------------------------------------------------------------

def crear_administrador(request):
    if request.method == 'POST':
        # Si la solicitud es POST, procesa el formulario
        form = AdministradorForm(request.POST, request.FILES)
        if form.is_valid():
            # Si el formulario es válido, guarda la nueva administrador en la base de datos
            administrador = form.save()
            return redirect('ver_administrador', pk=administrador.pk)
    else:
        # Si la solicitud no es POST, muestra un formulario en blanco para crear una nueva administrador
        form = AdministradorForm()
    return render(request, 'crear_administrador.html', {'form': form})

#-----------------------------------------------------------------------------------------------------

def editar_administrador(request, pk):
    # Recupera la administrador específica usando su clave primaria (pk)
    administrador = get_object_or_404(Administrador, pk=pk)
    if request.method == 'POST':
        # Si la solicitud es POST, procesa el formulario de edición
        form = AdministradorForm(request.POST, request.FILES, instance=administrador)
        if form.is_valid():
            # Si el formulario es válido, guarda los cambios en la administrador
            administrador = form.save()
            return redirect('ver_administrador', pk=administrador.pk)
    else:
        # Si la solicitud no es POST, muestra el formulario de edición con los datos actuales de la administrador
        form = AdministradorForm(instance=administrador)
    return render(request, 'editar_administrador.html', {'form': form, 'administrador': administrador})

#-----------------------------------------------------------------------------------------------------

def eliminar_administrador(request, pk):
    # Recupera la administrador específica usando su clave primaria (pk)
    administrador = get_object_or_404(Administrador, pk=pk)
    administrador.delete()
    return redirect('listar_administradores')

#-----------------------------------------------------------------------------------------------------

def inicio_administrador(request):
    # Esta función simplemente renderiza la página de inicio de la comunidad
    return render(request, 'inicio_administrador')

# Vista para visita***************************************************************************************************************************)6


def listar_visitas(request):
    visita = Visita.objects.all()
    return render(request, 'listar_visitas.html', {'visita': visita})

#-----------------------------------------------------------------------------------------------------

def ver_visita(request, pk):
    # Recupera la visita específica usando su clave primaria (pk)
    visita = get_object_or_404(Visita, pk=pk)
    return render(request, 'ver_visita.html', {'visita': visita})

#-----------------------------------------------------------------------------------------------------

def crear_visita(request):
    if request.method == 'POST':
        # Si la solicitud es POST, procesa el formulario
        form = VisitaForm(request.POST, request.FILES)
        if form.is_valid():
            # Si el formulario es válido, guarda la nueva visita en la base de datos
            visita = form.save()
            return redirect('ver_visita', pk=visita.pk)
    else:
        # Si la solicitud no es POST, muestra un formulario en blanco para crear una nueva visita
        form = VisitaForm()
    return render(request, 'crear_visita.html', {'form': form})

#-----------------------------------------------------------------------------------------------------

def editar_visita(request, pk):
    # Recupera la visita específica usando su clave primaria (pk)
    visita = get_object_or_404(Visita, pk=pk)
    if request.method == 'POST':
        # Si la solicitud es POST, procesa el formulario de edición
        form = VisitaForm(request.POST, request.FILES, instance=visita)
        if form.is_valid():
            # Si el formulario es válido, guarda los cambios en la visita
            visita = form.save()
            return redirect('ver_visita', pk=visita.pk)
    else:
        # Si la solicitud no es POST, muestra el formulario de edición con los datos actuales de la visita
        form = VisitaForm(instance=visita)
    return render(request, 'editar_visita.html', {'form': form, 'visita': visita})

#-----------------------------------------------------------------------------------------------------

def eliminar_visita(request, pk):
    # Recupera la visita específica usando su clave primaria (pk)
    visita = get_object_or_404(Visita, pk=pk)
    visita.delete()
    return redirect('listar_visitas')

#----------------------------------------------------------------------------------------------------->6

def inicio_visita(request):
    # Esta función simplemente renderiza la página de inicio de la comunidad
    return render(request, 'inicio_visita')