import re
from datetime import date

from dateutil.relativedelta import relativedelta
from django.core.validators import validate_email
from rest_framework import serializers

from . import models


class AdressSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Adress
        fields = [
            "user",
            "city",
            "state",
            "neighborhood",
            "number",
            "complement",
            "cep",
            "last_updated",
            "created",
        ]


class MeasurementsSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Measurements
        fields = [
            "user",
            "body_size",
            "foot",
            "last_updated",
            "created",
        ]


class UsuarioSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        style={"input_type": "password"},
        label="Senha",
        help_text="Sua senha deve ter pelo menos 8 caracteres.",
    )

    is_active = serializers.BooleanField(
        read_only=True,
        default=True,
    )

    date_joined = serializers.DateTimeField(read_only=True)
    last_updated = serializers.DateTimeField(read_only=True)
    last_login = serializers.DateTimeField(read_only=True)
    email = serializers.EmailField(validators=[validate_email])
    age = serializers.SerializerMethodField()

    address = AdressSerializer(required=False, many=False)

    class Meta:
        model = models.Usuario
        fields = [
            "id",
            "username",
            "password",
            "first_name",
            "last_name",
            "phone",
            "cpf",
            "gender",
            "email",
            "birth_date",
            "age",
            "photo",
            "social_medias",
            "is_active",
            "date_joined",
            "last_updated",
            "last_login",
            "address",
        ]

    def get_age(self, instance):
        if instance.birth_date:
            today = date.today()
            age = relativedelta(today, instance.birth_date).years
            return age

    def create(self, validated_data):
        address_data = validated_data.pop(
            "address", None
        )  # Extrai os dados de endereço, se houver
        user = models.Usuario.objects.create(**validated_data)

        if address_data:
            models.Adress.objects.create(
                user=user, **address_data
            )  # Cria o endereço associado ao usuário

        return user

    def update(self, instance, validated_data):
        # Update nested fields separately
        address_data = validated_data.pop("address", None)

        # Use the `setattr` function to iterate over validated_data
        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()

        if address_data:
            if hasattr(instance, "address"):
                # Update address instance
                for attr, value in address_data.items():
                    setattr(instance.address, attr, value)
                instance.address.save()
            else:
                # Create a new address if it does not exist
                models.Adress.objects.create(user=instance, **address_data)

        return instance

    def validate_cpf(self, value):
        """
        Valida o CPF usando o algoritmo de verificação.
        """
        cpf = re.sub(r"\D", "", value)

        if len(cpf) != 11 or cpf == cpf[0] * 11:
            raise serializers.ValidationError("CPF inválido.")

        def calcular_digito(cpf_parcial, peso_inicial):
            soma = sum(
                int(digito) * peso
                for digito, peso in zip(cpf_parcial, range(peso_inicial, 1, -1))
            )
            resto = soma % 11
            return "0" if resto < 2 else str(11 - resto)

        primeiro_digito = calcular_digito(cpf[:9], 10)
        segundo_digito = calcular_digito(cpf[:10], 11)

        if cpf[-2:] != primeiro_digito + segundo_digito:
            raise serializers.ValidationError("CPF inválido.")

        return value
