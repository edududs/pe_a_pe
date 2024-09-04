from rest_framework import viewsets, permissions

from . import serializers
from . import models


class AdressViewSet(viewsets.ModelViewSet):
    """ViewSet for the Adress class"""

    queryset = models.Adress.objects.all()
    serializer_class = serializers.AdressSerializer
    permission_classes = [permissions.IsAuthenticated]


class MeasurementsViewSet(viewsets.ModelViewSet):
    """ViewSet for the Measurements class"""

    queryset = models.Measurements.objects.all()
    serializer_class = serializers.MeasurementsSerializer
    permission_classes = [permissions.IsAuthenticated]


class UsuarioViewSet(viewsets.ModelViewSet):
    """ViewSet for the Usuario class"""

    queryset = models.Usuario.objects.all()
    serializer_class = serializers.UsuarioSerializer
    permission_classes = [permissions.IsAuthenticated]
