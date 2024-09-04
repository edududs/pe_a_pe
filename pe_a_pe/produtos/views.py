from django.views import generic
from django.urls import reverse_lazy
from . import models
from . import forms


class ProdutoListView(generic.ListView):
    model = models.Produto
    form_class = forms.ProdutoForm


class ProdutoCreateView(generic.CreateView):
    model = models.Produto
    form_class = forms.ProdutoForm


class ProdutoDetailView(generic.DetailView):
    model = models.Produto
    form_class = forms.ProdutoForm


class ProdutoUpdateView(generic.UpdateView):
    model = models.Produto
    form_class = forms.ProdutoForm
    pk_url_kwarg = "pk"


class ProdutoDeleteView(generic.DeleteView):
    model = models.Produto
    success_url = reverse_lazy("produtos_Produto_list")
