from django.db import models


class ProdutoQuerySet(models.QuerySet):
    def by_status(self, status):
        return self.filter(status__iexact=status)

    def by_size(self, size):
        return self.filter(size__iexact=size)

    def by_type(self, type_):
        return self.filter(type__iexact=type_)

    def by_condition(self, condition):
        return self.filter(condition__iexact=condition)

    def by_color(self, color):
        return self.filter(color__iexact=color)

    def by_name(self, name):
        return self.filter(name__iexact=name)

    def by_brand(self, brand):
        return self.filter(brand__iexact=brand)

    def recent(self):
        return self.order_by("-created")

    def updated_recently(self):
        return self.filter(last_updated__gte=models.F("created"))

    def size_range(self, min_size, max_size):
        return self.filter(size__gte=min_size, size__lte=max_size)
