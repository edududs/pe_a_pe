from django.db import models
from django.urls import reverse
from produtos import querysets


class ProductType(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return str(self.name)


class Produto(models.Model):

    # Relationships
    adress = models.ForeignKey(
        "usuarios.Adress", on_delete=models.CASCADE, related_name="product"
    )
    type = models.ForeignKey(
        ProductType,
        on_delete=models.CASCADE,
        related_name="product",
        null=True,
        blank=True,
    )

    class StatusChoices(models.TextChoices):
        ATIVO = "AT", "Ativo"
        INATIVO = "IN", "Inativo"
        PENDENTE = "PE", "Pendente"
        A_CAMINHO = "AC", "A caminho"
        ESGOTADO = "ES", "Esgotado"
        PROCESSANDO = "PR", "Em processamento"
        DESCONTINUADO = "DI", "Descontinuado"
        RESERVADO = "RE", "Reservado"
        DEVOLVIDO = "DE", "Devolvido"

    # Fields
    status = models.CharField(
        max_length=2, choices=StatusChoices.choices, default=StatusChoices.ATIVO
    )
    size = models.CharField(max_length=30, null=True, blank=True)
    condition = models.TextField(max_length=200, null=True, blank=True)
    color = models.CharField(max_length=200, null=True, blank=True)
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    brand = models.CharField(max_length=200, null=True, blank=True)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    objects = querysets.ProdutoQuerySet.as_manager()

    class Meta:
        pass

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse("produtos_Produto_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("produtos_Produto_update", args=(self.pk,))
