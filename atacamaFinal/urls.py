"""atacamaFinal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from kozanApp import views 

router=DefaultRouter()
router.register('trabajador',views.TrabajadorViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    #equipos
    path('equipos/',views.listadoEquipos),
    path('registrarEquipo/',views.agregarEquipo),
    path('eliminarEquipo/<int:id>',views.eliminarEquipo),
    path('actualizarEquipo/<int:id>',views.actualizarEquipo),
    #empleados
    path('empleados/', views.listadoEmpleados),
    path('agregarEmpleados/', views.agregarEmpleados),
    path('eliminarEmpleado/<int:id>', views.eliminarEmpleado),
    path('actualizarEmpleado/<int:id>', views.actualizarEmpleado),
    #areas
    path('areas/', views.listadoAreas),
    path('registrarArea/', views.agregarAreas),
    path('eliminarAreas/<int:id>', views.eliminarAreas),
    path('actualizarAreas/<int:id>', views.actualizarAreas),
    #api
    path('',include(router.urls)),
    
    path('trabajador2/', views.trabajador_list),
    path('trabajador2/<int:pk>', views.trabajador_detail),

    path('trabajador3/', views.TrabajadorList.as_view()),
    path('trabajador3/<int:pk>', views.TrabajadorDetail.as_view()),



]
