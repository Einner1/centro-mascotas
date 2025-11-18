from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='inicio'),
    path('inicio/', views.inicio, name='inicio'),  # Página de inicio

    # Fundaciones
    path('fundaciones/', views.FundacionListView.as_view(), name='fundacion_list'),
    path('fundaciones/nueva/', views.FundacionCreateView.as_view(), name='fundacion_create'),
    path('fundaciones/editar/<int:pk>/', views.FundacionUpdateView.as_view(), name='fundacion_update'),
    path('fundaciones/eliminar/<int:pk>/', views.FundacionDeleteView.as_view(), name='fundacion_delete'),

    # Mascotas
    path('mascotas/', views.MascotaListView.as_view(), name='mascota_list'),
    path('mascotas/nueva/', views.MascotaCreateView.as_view(), name='mascota_create'),
    path('mascotas/editar/<int:pk>/', views.MascotaUpdateView.as_view(), name='mascota_update'),
    path('mascotas/eliminar/<int:pk>/', views.MascotaDeleteView.as_view(), name='mascota_delete'),

    # Registro y login
    path('registro/', views.registro_usuario, name='registro_usuario'),
    path('login/', views.login_usuario, name='login_usuario'),
    path('logout/', views.logout_usuario, name='logout_usuario'),
    path('fundacion/<int:fundacion_id>/', views.fundacion_detalle, name='fundacion_detalle'),

    # Adoptar mascota
    path('adoptar/<int:mascota_id>/', views.adoptar_mascota, name='adoptar_mascota'),
]

