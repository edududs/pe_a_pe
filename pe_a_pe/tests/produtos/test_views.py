import pytest
import test_helpers

from django.urls import reverse


pytestmark = [pytest.mark.django_db]


def tests_Produto_list_view(client):
    instance1 = test_helpers.create_produtos_Produto()
    instance2 = test_helpers.create_produtos_Produto()
    url = reverse("produtos_Produto_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_Produto_create_view(client):
    adress = test_helpers.create_usuarios_Adress()
    url = reverse("produtos_Produto_create")
    data = {
        "status": "text",
        "size": "text",
        "type": "text",
        "condition": "text",
        "color": "text",
        "name": "text",
        "brand": "text",
        "adress": adress.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Produto_detail_view(client):
    instance = test_helpers.create_produtos_Produto()
    url = reverse("produtos_Produto_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_Produto_update_view(client):
    adress = test_helpers.create_usuarios_Adress()
    instance = test_helpers.create_produtos_Produto()
    url = reverse("produtos_Produto_update", args=[instance.pk, ])
    data = {
        "status": "text",
        "size": "text",
        "type": "text",
        "condition": "text",
        "color": "text",
        "name": "text",
        "brand": "text",
        "adress": adress.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302
