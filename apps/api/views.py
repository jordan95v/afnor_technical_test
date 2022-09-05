from typing import Any
from django.shortcuts import render
from django.views import generic
from django.http import HttpRequest, JsonResponse
from django.core.serializers import serialize
from django.core.exceptions import ObjectDoesNotExist
from django.forms.models import model_to_dict
from apps.api.models import Standard

# Create your views here.


class RecordView(generic.View):
    async def get(self, request: HttpRequest, numdos: str) -> JsonResponse:
        standard: Standard
        data: dict[str, Any] = dict()
        try:
            standard = await Standard.objects.aget(numdos=numdos)
        except ObjectDoesNotExist:
            data.update(dict(error="Object does not exists."))
        else:
            data.update(content=model_to_dict(standard))
        finally:
            return JsonResponse(data=data, safe=False)


class AllRecordView(generic.View):
    async def get(self, request: HttpRequest) -> JsonResponse:
        standards: list[Standard] = [
            standard async for standard in Standard.objects.all()
        ]
        data: list[dict[str, str]] = [model_to_dict(record) for record in standards]
        return JsonResponse(data=data, safe=False)
