from typing import Any
from django.views import generic
from django.http import HttpRequest, JsonResponse, HttpResponseNotFound
from django.core.exceptions import ObjectDoesNotExist
from django.forms.models import model_to_dict
from django.utils.datastructures import MultiValueDictKeyError
from apps.api.models import Standard

# Create your views here.


class RecordView(generic.View):
    async def get(self, request: HttpRequest, numdos: str) -> JsonResponse:
        standard: Standard
        data: dict[str, Any]
        try:
            standard = await Standard.objects.aget(numdos=numdos)
        except ObjectDoesNotExist:
            data = dict(error="Object does not exists.")
        else:
            data = dict(content=model_to_dict(standard))
        finally:
            return JsonResponse(data=data, safe=False)


class AllRecordView(generic.View):
    async def get(self, request: HttpRequest) -> JsonResponse:
        standards: list[Standard] = [
            standard async for standard in Standard.objects.all()
        ]
        data: dict[str, Any] | list[dict[str, str]]
        try:
            page: int = int(request.GET["page"])
            data = [
                model_to_dict(record)
                for record in standards[(page - 1) * 100 : page * 100]
            ]
        except MultiValueDictKeyError:
            data = dict(error="No page requested.")
        finally:
            return JsonResponse(data=data, safe=False)
