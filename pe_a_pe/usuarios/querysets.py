from datetime import date

from django.contrib.auth.models import UserManager
from django.db import models


class UsuarioManager(UserManager):
    def get_queryset(self):
        return UsuarioQuerySet(self.model, using=self._db)


class UsuarioQuerySet(models.QuerySet):
    def with_photo(self):
        return self.exclude(photo__isnull=True)

    def by_gender(self, gender):
        return self.filter(gender__iexact=gender)

    def by_birth_year(self, year):
        return self.filter(birth_date__year=year)

    def by_phone(self, phone):
        return self.filter(phone__iexact=phone)

    def no_cpf(self):
        return self.filter(cpf__isnull=True)

    def age_between(self, min_age, max_age):
        today = date.today()
        min_birth_date = today.replace(year=today.year - max_age - 1)
        max_birth_date = today.replace(year=today.year - min_age)
        return self.filter(birth_date__range=(min_birth_date, max_birth_date))


class AdressQuerySet(models.QuerySet):
    def by_state(self, state):
        return self.filter(state__iexact=state)

    def by_city(self, city):
        return self.filter(city__iexact=city)

    def by_cep(self, cep):
        return self.filter(cep__iexact=cep)

    def recent(self):
        return self.order_by("-created")

    def updated_recently(self):
        return self.filter(last_updated__gte=models.F("created"))


class MeasurementsQuerySet(models.QuerySet):
    def by_body_size(self, body_size):
        return self.filter(body_size__iexact=body_size)

    def by_foot_size(self, foot_size):
        return self.filter(foot__exact=foot_size)

    def body_size_range(self, min_size, max_size):
        return self.filter(body_size__gte=min_size, body_size__lte=max_size)

    def updated_recently(self):
        return self.filter(last_updated__gte=models.F("created"))
