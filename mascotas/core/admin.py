from django.contrib import admin
from .models import Fundacion, Mascota, Adopcion
from django.contrib.auth.admin import UserAdmin
from .models import Usuario, Fundacion, Mascota, Adopcion



@admin.register(Usuario)
class CustomUserAdmin(UserAdmin):
    model = Usuario
    list_display = ('username', 'email', 'is_active', 'is_staff')
    list_filter = ('is_active', 'is_staff')
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Información personal', {'fields': ('telefono', 'direccion')}),
        ('Permisos', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'telefono', 'direccion', 'is_active', 'is_staff')}
        ),
    )
    search_fields = ('username', 'email')
    ordering = ('username',)

@admin.register(Fundacion)
class FundacionAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'telefono', 'email', 'capacidad')

@admin.register(Mascota)
class MascotaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'especie', 'fundacion', 'disponible')

@admin.register(Adopcion)
class AdopcionAdmin(admin.ModelAdmin):
    list_display = ('mascota', 'usuario', 'fundacion', 'fecha_adopcion')

