from django.contrib import admin
from django import forms

from . import models


class ProdutoAdminForm(forms.ModelForm):

    class Meta:
        model = models.Produto
        fields = "__all__"


class ProdutoAdmin(admin.ModelAdmin):
    form = ProdutoAdminForm
    list_display = [
        "status",
        "size",
        "type",
        "condition",
        "color",
        "name",
        "created",
        "brand",
        "last_updated",
    ]
    readonly_fields = [
        "status",
        "size",
        "type",
        "condition",
        "color",
        "name",
        "created",
        "brand",
        "last_updated",
    ]


admin.site.register(models.Produto, ProdutoAdmin)
