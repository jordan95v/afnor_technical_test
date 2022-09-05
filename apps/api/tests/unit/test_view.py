from typing import Any
import pytest
from django.test import Client
from django.urls import reverse
from django.http import JsonResponse
from apps.api.models import Standard


@pytest.mark.django_db
class TestView:
    def test_get_all_error(self):
        client: Client = Client()
        res: JsonResponse = client.get("/get/")
        assert "error" in res.json()

    def test_get_all(self):
        client: Client = Client()
        res: JsonResponse = client.get("/get/", data=dict(page=1))
        assert isinstance(res.json(), list)

    def test_get_single(self):
        Standard.objects.create(numdos="FA010203")
        client: Client = Client()
        res: JsonResponse = client.get("/get/FA010203/")
        ret: dict[str, Any] = res.json()["content"]
        assert ret["numdos"] == "FA010203"

    def test_get_single_fail(self):
        Standard.objects.create(numdos="FA010203")
        client: Client = Client()
        res: JsonResponse = client.get("/get/hello/")
        assert "error" in res.json()
