from django.views import generic
from django.urls import reverse_lazy
from . import models
from . import forms


class AdressListView(generic.ListView):
    model = models.Adress
    form_class = forms.AdressForm


class AdressCreateView(generic.CreateView):
    model = models.Adress
    form_class = forms.AdressForm


class AdressDetailView(generic.DetailView):
    model = models.Adress
    form_class = forms.AdressForm


class AdressUpdateView(generic.UpdateView):
    model = models.Adress
    form_class = forms.AdressForm
    pk_url_kwarg = "pk"


class AdressDeleteView(generic.DeleteView):
    model = models.Adress
    success_url = reverse_lazy("usuarios_Adress_list")


class MeasurementsListView(generic.ListView):
    model = models.Measurements
    form_class = forms.MeasurementsForm


class MeasurementsCreateView(generic.CreateView):
    model = models.Measurements
    form_class = forms.MeasurementsForm


class MeasurementsDetailView(generic.DetailView):
    model = models.Measurements
    form_class = forms.MeasurementsForm


class MeasurementsUpdateView(generic.UpdateView):
    model = models.Measurements
    form_class = forms.MeasurementsForm
    pk_url_kwarg = "pk"


class MeasurementsDeleteView(generic.DeleteView):
    model = models.Measurements
    success_url = reverse_lazy("usuarios_Measurements_list")


class UsuarioListView(generic.ListView):
    model = models.Usuario
    form_class = forms.UsuarioForm


class UsuarioCreateView(generic.CreateView):
    model = models.Usuario
    form_class = forms.UsuarioForm


class UsuarioDetailView(generic.DetailView):
    model = models.Usuario
    form_class = forms.UsuarioForm


class UsuarioUpdateView(generic.UpdateView):
    model = models.Usuario
    form_class = forms.UsuarioForm
    pk_url_kwarg = "pk"


class UsuarioDeleteView(generic.DeleteView):
    model = models.Usuario
    success_url = reverse_lazy("usuarios_Usuario_list")
