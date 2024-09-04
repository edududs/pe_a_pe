from django.contrib import admin
from django import forms

from . import models


class AdressAdminForm(forms.ModelForm):

    class Meta:
        model = models.Adress
        fields = "__all__"


class AdressAdmin(admin.ModelAdmin):
    form = AdressAdminForm
    list_display = [
        "complement",
        "state",
        "city",
        "cep",
        "last_updated",
        "neighborhood",
        "created",
        "number",
    ]
    readonly_fields = [
        "complement",
        "state",
        "city",
        "cep",
        "last_updated",
        "neighborhood",
        "created",
        "number",
    ]


class MeasurementsAdminForm(forms.ModelForm):

    class Meta:
        model = models.Measurements
        fields = "__all__"


class MeasurementsAdmin(admin.ModelAdmin):
    form = MeasurementsAdminForm
    list_display = [
        "body_size",
        "foot",
        "last_updated",
        "created",
    ]
    readonly_fields = [
        "body_size",
        "foot",
        "last_updated",
        "created",
    ]


class UsuarioAdminForm(forms.ModelForm):

    class Meta:
        model = models.Usuario
        fields = "__all__"


class UsuarioAdmin(admin.ModelAdmin):
    form = UsuarioAdminForm
    list_display = [
        "last_updated",
        "photo",
        "phone",
        "cpf",
        "birth_date",
        "date_joined",
        "gender",
        "social_medias",
    ]
    readonly_fields = [
        "last_updated",
        "photo",
        "phone",
        "cpf",
        "birth_date",
        "date_joined",
        "gender",
        "social_medias",
    ]


admin.site.register(models.Adress, AdressAdmin)
admin.site.register(models.Measurements, MeasurementsAdmin)
admin.site.register(models.Usuario, UsuarioAdmin)
