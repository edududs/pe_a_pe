from rest_framework import viewsets, permissions

from . import serializers
from . import models


class ProdutoViewSet(viewsets.ModelViewSet):
    """ViewSet for the Produto class"""

    queryset = models.Produto.objects.all()
    serializer_class = serializers.ProdutoSerializer
    permission_classes = [permissions.IsAuthenticated]
