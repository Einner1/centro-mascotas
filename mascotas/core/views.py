from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Fundacion, Mascota, Adopcion
from .forms import RegistroUsuarioForm


# Vista de index/landing page (sin login requerido)
def index(request):
    """Página principal pública - landing page"""
    if request.user.is_authenticated:
        return redirect('inicio')
    return render(request, 'core/index.html')


# Vista de inicio después de login
@login_required(login_url='login_usuario')
def inicio(request):
    """Dashboard/inicio para usuarios autenticados"""
    usuario = request.user
    fundaciones = Fundacion.objects.all()
    mascotas_disponibles = Mascota.objects.filter(disponible=True)

    context = {
        'usuario': usuario,
        'fundaciones': fundaciones,
        'mascotas_disponibles': mascotas_disponibles
    }
    return render(request, 'core/inicio.html', context)

@login_required
def fundacion_detalle(request, fundacion_id):
    """Vista para mostrar todos los animales de una fundación"""
    fundacion = get_object_or_404(Fundacion, id=fundacion_id)
    mascotas = Mascota.objects.filter(fundacion=fundacion)
    
    context = {
        'fundacion': fundacion,
        'mascotas': mascotas,
        'usuario': request.user,
    }
    return render(request, 'core/fundacion_detalle.html', context)






# Login
def login_usuario(request):
    # Si ya está autenticado, ir directo a inicio
    if request.user.is_authenticated:
        return redirect('inicio')
    
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        print(f"=== DEBUG LOGIN ===")
        print(f"Email recibido: {email}")
        print(f"Password recibido: {'***' if password else 'None'}")
        
        # Autenticar usuario
        usuario = authenticate(request, email=email, password=password)
        
        print(f"Usuario autenticado: {usuario}")
        
        if usuario is not None:
            # Login exitoso
            login(request, usuario)
            print(f"Login exitoso para: {usuario.username}")
            print(f"Usuario autenticado después de login: {request.user.is_authenticated}")
            
            messages.success(request, f'¡Bienvenido {usuario.username}!')
            return redirect('inicio')
        else:
            print("Autenticación falló")
            messages.error(request, 'Correo o contraseña incorrectos.')
    
    return render(request, 'core/login.html')


# Registro
def registro_usuario(request):
    if request.user.is_authenticated:
        return redirect('inicio')
    
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            login(request, usuario)
            messages.success(request, 'Tu cuenta ha sido creada correctamente.')
            return redirect('inicio')
        else:
            for error in form.errors.values():
                messages.error(request, error)
    else:
        form = RegistroUsuarioForm()
    
    return render(request, 'core/registro_usuario.html', {'form': form})


# Logout
def logout_usuario(request):
    logout(request)
    messages.info(request, 'Has cerrado sesión correctamente.')
    return redirect('login_usuario')


# Adoptar mascota
@login_required(login_url='login_usuario')
def adoptar_mascota(request, mascota_id):
    """Permite a un usuario adoptar una mascota disponible."""
    mascota = get_object_or_404(Mascota, id=mascota_id)

    if not mascota.disponible:
        messages.error(request, f"La mascota {mascota.nombre} ya fue adoptada.")
        return redirect('inicio')

    # Crear adopción
    adopcion = Adopcion.objects.create(
        mascota=mascota,
        usuario=request.user,
        fundacion=mascota.fundacion
    )

    # Marcar mascota como no disponible
    mascota.disponible = False
    mascota.save()

    messages.success(request, f"¡Has adoptado a {mascota.nombre} correctamente!")
    return redirect('inicio')


# -------- FUNDACIONES --------
class FundacionListView(ListView):
    model = Fundacion
    template_name = 'core/fundacion_list.html'
    context_object_name = 'fundaciones'


class FundacionCreateView(CreateView):
    model = Fundacion
    fields = '__all__'
    template_name = 'core/fundacion_form.html'
    success_url = reverse_lazy('fundacion_list')


class FundacionUpdateView(UpdateView):
    model = Fundacion
    fields = '__all__'
    template_name = 'core/fundacion_form.html'
    success_url = reverse_lazy('fundacion_list')


class FundacionDeleteView(DeleteView):
    model = Fundacion
    template_name = 'core/fundacion_confirm_delete.html'
    success_url = reverse_lazy('fundacion_list')


# -------- MASCOTAS --------
class MascotaListView(ListView):
    model = Mascota
    template_name = 'core/mascota_list.html'
    context_object_name = 'mascotas'


class MascotaCreateView(CreateView):
    model = Mascota
    fields = '__all__'
    template_name = 'core/mascota_form.html'
    success_url = reverse_lazy('mascota_list')


class MascotaUpdateView(UpdateView):
    model = Mascota
    fields = '__all__'
    template_name = 'core/mascota_form.html'
    success_url = reverse_lazy('mascota_list')


class MascotaDeleteView(DeleteView):
    model = Mascota
    template_name = 'core/mascota_confirm_delete.html'
    success_url = reverse_lazy('mascota_list')