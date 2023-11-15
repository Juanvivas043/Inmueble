from django.urls import path 
from inmuebleslist_app.api.views import EdificacionListAV, EdificacionDetalleAV, EmpresaAV


urlpatterns = [
    
    path('list/', EdificacionListAV.as_view(), name='edificacion_list'),
    path('<int:pk>/', EdificacionDetalleAV.as_view(), name='edificacion_detalle'),
    path('empresa/', EmpresaAV.as_view(), name='empresa_list'),
]