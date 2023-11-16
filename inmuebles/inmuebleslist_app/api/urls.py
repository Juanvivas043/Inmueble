from django.urls import path 
from inmuebleslist_app.api.views import (EdificacionListAV, EdificacionDetalleAV, EmpresaAV, EmpresaDetalleAV, 
                                         ComentarioList, ComentarioDetail, ComentarioCreate)


urlpatterns = [
    
    path('edificacion/', EdificacionListAV.as_view(), name='edificacion-list'),
    path('edificacion/<int:pk>/', EdificacionDetalleAV.as_view(), name='edificacion-detail'),
    
    path('empresa/', EmpresaAV.as_view(), name='empresa-list'),
    path('empresa/<int:pk>', EmpresaDetalleAV.as_view(), name='empresa-detail'),
    
    path('edificacion/<int:pk>/comentario-create/', ComentarioCreate.as_view(), name='comentario-create'),
    path('edificacion/<int:pk>/comentario/', ComentarioList.as_view(), name='comentario-list'),
    path('edificacion/comentario/<int:pk>', ComentarioDetail.as_view(), name='comentario-detail'),
    

]