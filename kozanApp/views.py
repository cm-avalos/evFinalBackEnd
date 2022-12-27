from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from kozanApp.forms import FormEmpleado,FormEquipo, FormArea
from kozanApp.models import Empleado,Equipos,Area
from . import forms
#api
from django.shortcuts import render
from .serializers import EmpleadoSerializer
from .models import Empleado
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.http import Http404
from rest_framework import generics,viewsets,mixins
from rest_framework.decorators import APIView




def index(request):
    return render(request, 'kozanApp/index.html')

def listadoEmpleados(request):
    empleados = Empleado.objects.all()
    data = {'empleados': empleados}
    return render(request, 'kozanApp/empleados.html', data)

def agregarEmpleados(request):
    form = FormEmpleado()
    if request.method == 'POST':
        form = FormEmpleado(request.POST)
        if form.is_valid():
            form.save()
        return index(request)
    data = {'form' : form}
    return render(request, 'kozanApp/agregarEmpleados.html', data)

def eliminarEmpleado(request, id):
    empleado = Empleado.objects.get(id = id)
    empleado.delete()
    return redirect('/empleados',)

def actualizarEmpleado(request, id):
    empleado = Empleado.objects.get(id = id)
    form = FormEmpleado(instance=empleado)
    if request.method == 'POST':
        form = FormEmpleado(request.POST, instance=empleado)
        if form.is_valid():
            form.save()
        return index(request)
    data = {'form' : form}
    return render(request, 'kozanApp/agregarEmpleados.html', data)

    ############################################################################################################################

    #equipo

    #############################################################################################################################



def listadoEquipos(request):
    equipos = Equipos.objects.all()
    data = {"equipos":equipos}
    return render(request,'kozanApp/equipos.html',data)

def agregarEquipo(request):
    form = FormEquipo()
    if request.method == 'POST':
        form = FormEquipo(request.POST)
        if form.is_valid():
            form.save()
        return index(request)
    data={'form':form}
    return render(request,'kozanApp/registrarEquipo.html',data)


def eliminarEquipo(request,id):
    equipos=Equipos.objects.get(id=id)
    equipos.delete()
    return redirect('/equipos')


def actualizarEquipo(request,id):
    equipo = Equipos.objects.get(id=id)
    form = FormEquipo(instance=equipo)
    if request.method == 'POST':
        form = FormEquipo(request.POST, instance=equipo)
        if form.is_valid():
            form.save()
        return index(request)
    data={'form':form}
    return render(request,'kozanApp/registrarEquipo.html',data)

    ############################################################################################################################

    #areas

    #############################################################################################################################


def listadoAreas(request):
    areas = Area.objects.all()
    data = {'areas': areas}
    return render(request, 'kozanApp/areas.html', data)

def agregarAreas(request):
    form = FormArea()
    if request.method == 'POST':
        form = FormArea(request.POST)
        if form.is_valid():
            form.save()
        return index(request)
    data = {'form' : form}
    return render(request, 'kozanApp/registrarArea.html', data)

def eliminarAreas(request, id):
    area = Area.objects.get(id = id)
    area.delete()
    return redirect('/areas',)

def actualizarAreas(request, id):
    area = Area.objects.get(id = id)
    form = FormArea(instance=area)
    if request.method == 'POST':
        form = FormArea(request.POST, instance=area)
        if form.is_valid():
            form.save()
        return index(request)
    data = {'form' : form}
    return render(request, 'kozanApp/registrarArea.html', data)



    #api_________________________________________________________________________________________________

    
# Create your views here.





@api_view(['GET', 'POST'])
def trabajador_list(request):
    if request.method == 'GET':
        empleados= Empleado.objects.all()
        serializer= EmpleadoSerializer(empleados, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer=EmpleadoSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def trabajador_detail(request,pk):
    try:
        trabajador = Empleado.objects.get(pk=pk)
    except Empleado.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer= EmpleadoSerializer(trabajador)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = EmpleadoSerializer(trabajador, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        trabajador.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
#___________________________________________________________________________________________________________________________________
 

class TrabajadorList(APIView):

    def get(self,request):
        trabajador= Empleado.objects.all()
        serializer= EmpleadoSerializer(trabajador, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer= EmpleadoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TrabajadorDetail(APIView):
    def get_object(self,pk):
        try:
            return Empleado.objects.get(pk=pk)
        except Empleado.DoesNotExist:
            return Http404

    def get(self,request,pk):
        trabajador= self.get_object(pk)
        serializer= EmpleadoSerializer(trabajador)
        return Response(serializer.data)

    def put(self,request,pk):
        trabajador= self.get_object(pk)
        serializer= EmpleadoSerializer(trabajador, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self,request,pk):
        trabajador= self.get_object(pk)
        trabajador.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    ############################################################

class TrabajadorListt(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset= Empleado.objects.all()
    serializer_class=EmpleadoSerializer


    def get(self,request):
        return self.list(request)

    def post(self,request):
        return self.create(request)

class TrabajadorDetaill(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin,generics.GenericAPIView):
    queryset= Empleado.objects.all()
    serializer_class=EmpleadoSerializer

    
    def get(self,request,pk):
        return self.retrieve(request,pk)

        
    def put(self,request,pk):
        return self.update(request,pk)

    def delete(self,request,pk):
        return self.destroy(request,pk)

    


#######################################33
class TrabajadorList(generics.ListCreateAPIView):
    queryset= Empleado.objects.all()
    serializer_class=EmpleadoSerializer

class TrabajadorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset= Empleado.objects.all()
    serializer_class=EmpleadoSerializer

#_________________________________-

class TrabajadorViewSet(viewsets.ModelViewSet):
    queryset= Empleado.objects.all()
    serializer_class=EmpleadoSerializer

    

