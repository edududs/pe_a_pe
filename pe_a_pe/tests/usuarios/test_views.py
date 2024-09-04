import pytest
import test_helpers

from django.urls import reverse


pytestmark = [pytest.mark.django_db]


def tests_Adress_list_view(client):
    instance1 = test_helpers.create_usuarios_Adress()
    instance2 = test_helpers.create_usuarios_Adress()
    url = reverse("usuarios_Adress_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_Adress_create_view(client):
    user = test_helpers.create_usuarios_Usuario()
    url = reverse("usuarios_Adress_create")
    data = {
        "complement": "text",
        "state": "text",
        "city": "text",
        "cep": "text",
        "neighborhood": "text",
        "number": "text",
        "user": user.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Adress_detail_view(client):
    instance = test_helpers.create_usuarios_Adress()
    url = reverse("usuarios_Adress_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_Adress_update_view(client):
    user = test_helpers.create_usuarios_Usuario()
    instance = test_helpers.create_usuarios_Adress()
    url = reverse("usuarios_Adress_update", args=[instance.pk, ])
    data = {
        "complement": "text",
        "state": "text",
        "city": "text",
        "cep": "text",
        "neighborhood": "text",
        "number": "text",
        "user": user.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Measurements_list_view(client):
    instance1 = test_helpers.create_usuarios_Measurements()
    instance2 = test_helpers.create_usuarios_Measurements()
    url = reverse("usuarios_Measurements_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_Measurements_create_view(client):
    user = test_helpers.create_usuarios_Usuario()
    url = reverse("usuarios_Measurements_create")
    data = {
        "body_size": "text",
        "foot": 1,
        "user": user.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Measurements_detail_view(client):
    instance = test_helpers.create_usuarios_Measurements()
    url = reverse("usuarios_Measurements_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_Measurements_update_view(client):
    user = test_helpers.create_usuarios_Usuario()
    instance = test_helpers.create_usuarios_Measurements()
    url = reverse("usuarios_Measurements_update", args=[instance.pk, ])
    data = {
        "body_size": "text",
        "foot": 1,
        "user": user.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Usuario_list_view(client):
    instance1 = test_helpers.create_usuarios_Usuario()
    instance2 = test_helpers.create_usuarios_Usuario()
    url = reverse("usuarios_Usuario_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_Usuario_create_view(client):
    url = reverse("usuarios_Usuario_create")
    data = {
        "photo": "anImage",
        "phone": "text",
        "cpf": "text",
        "birth_date": datetime.now(),
        "gender": "text",
        "social_medias": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Usuario_detail_view(client):
    instance = test_helpers.create_usuarios_Usuario()
    url = reverse("usuarios_Usuario_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_Usuario_update_view(client):
    instance = test_helpers.create_usuarios_Usuario()
    url = reverse("usuarios_Usuario_update", args=[instance.pk, ])
    data = {
        "photo": "anImage",
        "phone": "text",
        "cpf": "text",
        "birth_date": datetime.now(),
        "gender": "text",
        "social_medias": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302
