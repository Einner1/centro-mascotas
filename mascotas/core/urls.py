from django.urls import path
from . import views

urlpatterns = [
    # Rutas públicas
    path('', views.index, name='index'),
    path('login/', views.login_usuario, name='login_usuario'),
    path('registro/', views.registro_usuario, name='registro_usuario'),
    path('logout/', views.logout_usuario, name='logout_usuario'),
    
    # Rutas autenticadas
    path('inicio/', views.inicio, name='inicio'),
    path('fundacion/<int:fundacion_id>/', views.fundacion_detalle, name='fundacion_detalle'),
    path('adoptar/<int:mascota_id>/', views.adoptar_mascota, name='adoptar_mascota'),
    
    # Nueva ruta para factura
    path('factura/<int:adopcion_id>/', views.factura_adopcion, name='factura_adopcion'),
    
    # Nueva ruta para ver mis adopciones
    path('mis-adopciones/', views.mis_adopciones, name='mis_adopciones'),
    
    # CRUD Fundaciones
    path('fundaciones/', views.FundacionListView.as_view(), name='fundacion_list'),
    path('fundaciones/nueva/', views.FundacionCreateView.as_view(), name='fundacion_create'),
    path('fundaciones/<int:pk>/editar/', views.FundacionUpdateView.as_view(), name='fundacion_update'),
    path('fundaciones/<int:pk>/eliminar/', views.FundacionDeleteView.as_view(), name='fundacion_delete'),
    
    # CRUD Mascotas
    path('mascotas/', views.MascotaListView.as_view(), name='mascota_list'),
    path('mascotas/nueva/', views.MascotaCreateView.as_view(), name='mascota_create'),
    path('mascotas/<int:pk>/editar/', views.MascotaUpdateView.as_view(), name='mascota_update'),
    path('mascotas/<int:pk>/eliminar/', views.MascotaDeleteView.as_view(), name='mascota_delete'),
]