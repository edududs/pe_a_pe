from django import forms
from usuarios.models import Adress
from . import models


class ProdutoForm(forms.ModelForm):
    class Meta:
        model = models.Produto
        fields = [
            "status",
            "size",
            "type",
            "condition",
            "color",
            "name",
            "brand",
            "adress",
        ]

    def __init__(self, *args, **kwargs):
        super(ProdutoForm, self).__init__(*args, **kwargs)
        self.fields["adress"].queryset = Adress.objects.all()
