from django.urls import path 
from inmuebleslist_app.api.views import EdificacionListAV, EdificacionDetalleAV, EmpresaAV, EmpresaDetalleAV


urlpatterns = [
    
    path('list/', EdificacionListAV.as_view(), name='edificacion-list'),
    path('<int:pk>/', EdificacionDetalleAV.as_view(), name='edificacion-detail'),
    path('empresa/', EmpresaAV.as_view(), name='empresa-list'),
    path('empresa/<int:pk>', EmpresaDetalleAV.as_view(), name='empresa-detail'),

]