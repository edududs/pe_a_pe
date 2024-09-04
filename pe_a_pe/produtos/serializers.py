from rest_framework import serializers

from . import models


class ProdutoSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Produto
        fields = [
            "name",
            "status",
            "size",
            "type",
            "condition",
            "color",
            "created",
            "brand",
            "last_updated",
            "adress",
        ]
