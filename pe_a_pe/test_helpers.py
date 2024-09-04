import random
import string

from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import Group
from django.contrib.contenttypes.models import ContentType
from datetime import datetime

from usuarios import models as usuarios_models
from produtos import models as produtos_models


def random_string(length=10):
    # Create a random string of length length
    letters = string.ascii_lowercase
    return "".join(random.choice(letters) for i in range(length))


def create_User(**kwargs):
    defaults = {
        "username": "%s_username" % random_string(5),
        "email": "%s_username@tempurl.com" % random_string(5),
    }
    defaults.update(**kwargs)
    return User.objects.create(**defaults)


def create_AbstractUser(**kwargs):
    defaults = {
        "username": "%s_username" % random_string(5),
        "email": "%s_username@tempurl.com" % random_string(5),
    }
    defaults.update(**kwargs)
    return AbstractUser.objects.create(**defaults)


def create_AbstractBaseUser(**kwargs):
    defaults = {
        "username": "%s_username" % random_string(5),
        "email": "%s_username@tempurl.com" % random_string(5),
    }
    defaults.update(**kwargs)
    return AbstractBaseUser.objects.create(**defaults)


def create_Group(**kwargs):
    defaults = {
        "name": "%s_group" % random_string(5),
    }
    defaults.update(**kwargs)
    return Group.objects.create(**defaults)


def create_ContentType(**kwargs):
    defaults = {
    }
    defaults.update(**kwargs)
    return ContentType.objects.create(**defaults)


def create_usuarios_Adress(**kwargs):
    defaults = {}
    defaults["complement"] = ""
    defaults["state"] = ""
    defaults["city"] = ""
    defaults["cep"] = ""
    defaults["neighborhood"] = ""
    defaults["number"] = ""
    if "user" not in kwargs:
        defaults["user"] = create_usuarios_Usuario()
    defaults.update(**kwargs)
    return usuarios_models.Adress.objects.create(**defaults)
def create_usuarios_Measurements(**kwargs):
    defaults = {}
    defaults["body_size"] = ""
    defaults["foot"] = ""
    if "user" not in kwargs:
        defaults["user"] = create_usuarios_Usuario()
    defaults.update(**kwargs)
    return usuarios_models.Measurements.objects.create(**defaults)
def create_usuarios_Usuario(**kwargs):
    defaults = {}
    defaults["photo"] = ""
    defaults["phone"] = ""
    defaults["cpf"] = ""
    defaults["birth_date"] = datetime.now()
    defaults["gender"] = ""
    defaults["social_medias"] = ""
    defaults["username"] = "username"
    defaults["email"] = "username@tempurl.com"
    defaults.update(**kwargs)
    return usuarios_models.Usuario.objects.create(**defaults)
def create_produtos_Produto(**kwargs):
    defaults = {}
    defaults["status"] = ""
    defaults["size"] = ""
    defaults["type"] = ""
    defaults["condition"] = ""
    defaults["color"] = ""
    defaults["name"] = ""
    defaults["brand"] = ""
    if "adress" not in kwargs:
        defaults["adress"] = create_usuarios_Adress()
    defaults.update(**kwargs)
    return produtos_models.Produto.objects.create(**defaults)
