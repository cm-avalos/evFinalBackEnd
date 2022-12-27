from django import forms
from kozanApp.models import Equipos,Empleado,Area

    ############################################################################################################################

    #equipos

    #############################################################################################################################

class FormEquipo(forms.ModelForm):
    class Meta:
        model=Equipos
        fields='__all__'

    marca = forms.CharField(max_length=50)
    modelo = forms.CharField(max_length=50)
    procesador = forms.CharField(max_length=50)
    grafica = forms.CharField(max_length=50)
    memoria= forms.CharField(max_length=50)
    nequipo=forms.CharField(max_length=50)

    ############################################################################################################################

    #empleado

    #############################################################################################################################


class FormEmpleado(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = '__all__'

    nombre = forms.CharField(min_length=5, max_length=20)
    telefono = forms.CharField(min_length=5, max_length=20)
    cargo = forms.CharField(required=True)

    def clean_correo(self):
        inputCorreo = self.cleaned_data['correo']
        if inputCorreo.find('@') == -1:
            raise forms.ValidationError("El correo debe contener @")
        return inputCorreo


    ############################################################################################################################

    #areas

    #############################################################################################################################
class FormArea(forms.ModelForm):
        
    class Meta:
        model=Area
        fields='__all__'

    nombreArea = forms.CharField(max_length=50)
    encargado = forms.CharField(max_length=50)
    piso = forms.CharField(max_length=50)
    sector = forms.CharField(max_length=50)
    descripcion = forms.CharField(max_length=50)
    capacitacion = forms.CharField(max_length=2)