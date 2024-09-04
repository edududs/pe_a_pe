from django import forms
from usuarios.models import Usuario
from usuarios.models import Usuario
from . import models


class AdressForm(forms.ModelForm):
    class Meta:
        model = models.Adress
        fields = [
            "complement",
            "state",
            "city",
            "cep",
            "neighborhood",
            "number",
            "user",
        ]

    def __init__(self, *args, **kwargs):
        super(AdressForm, self).__init__(*args, **kwargs)
        self.fields["user"].queryset = Usuario.objects.all()



class MeasurementsForm(forms.ModelForm):
    class Meta:
        model = models.Measurements
        fields = [
            "body_size",
            "foot",
            "user",
        ]

    def __init__(self, *args, **kwargs):
        super(MeasurementsForm, self).__init__(*args, **kwargs)
        self.fields["user"].queryset = Usuario.objects.all()



class UsuarioForm(forms.ModelForm):
    class Meta:
        model = models.Usuario
        fields = [
            "photo",
            "phone",
            "cpf",
            "birth_date",
            "gender",
            "social_medias",
        ]
