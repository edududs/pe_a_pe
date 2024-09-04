from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser
from usuarios import querysets


class Adress(models.Model):

    # Relationships
    user = models.ForeignKey("usuarios.Usuario", on_delete=models.CASCADE, related_name='adresses')

    # Fields
    complement = models.CharField(max_length=200, null=True, blank=True)
    state = models.CharField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=200, null=True, blank=True)
    cep = models.CharField(max_length=8, null=True, blank=True)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    neighborhood = models.CharField(max_length=200, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    number = models.CharField(max_length=10, null=True, blank=True)
    
    objects = querysets.AdressQuerySet.as_manager()

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("usuarios_adress_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("usuarios_adress_update", args=(self.pk,))



class Measurements(models.Model):

    # Relationships
    user = models.ForeignKey("usuarios.Usuario", on_delete=models.CASCADE, related_name='measurements')

    # Fields
    body_size = models.CharField(max_length=30, null=True, blank=True)
    foot = models.IntegerField(null=True, blank=True)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    
    objects = querysets.MeasurementsQuerySet.as_manager()

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("usuarios_measurements_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("usuarios_measurements_update", args=(self.pk,))



class Usuario(AbstractUser):

    # Fields
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    photo = models.ImageField(upload_to="upload/images/", null=True, blank=True)
    phone = models.CharField(max_length=11, unique=True)
    cpf = models.CharField(max_length=11, unique=True)
    birth_date = models.DateField(null=True)
    gender = models.CharField(max_length=200, null=True, blank=True)
    social_medias = models.TextField(max_length=200, null=True, blank=True)
    
    objects = querysets.UsuarioManager()

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("usuarios_usuario_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("usuarios_usuario_update", args=(self.pk,))

