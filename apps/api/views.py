from typing import Any
from django.views import generic
from django.http import HttpRequest, JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from django.forms.models import model_to_dict
from django.utils.datastructures import MultiValueDictKeyError
from apps.api.models import Standard

# Create your views here.

__all__: list[str] = ["RecordView", "AllRecordView"]


class RecordView(generic.View):
    async def get(self, request: HttpRequest, numdos: str) -> JsonResponse:
        standard: Standard
        data: dict[str, Any]
        try:
            standard = await Standard.objects.aget(numdos=numdos)
        except ObjectDoesNotExist:
            data = dict(error="Object does not exists.")
        else:
            standard_dict: dict[str, Any] = model_to_dict(standard)
            standard_dict["supports"] = [
                model_to_dict(support) async for support in standard.support.all()
            ]
            data = dict(content=standard_dict)
        finally:
            return JsonResponse(data=data, safe=False)


class AllRecordView(generic.View):
    async def get(self, request: HttpRequest) -> JsonResponse:
        standards: list[Standard] = [
            standard async for standard in Standard.objects.all()
        ]
        data: list[dict[str, Any]] = []
        try:
            page: int = int(request.GET["page"])
            for standard in standards[(page - 1) * 100 : page * 100]:
                data.append(
                    dict(
                        standard=model_to_dict(standard),
                        supports=[
                            model_to_dict(support)
                            async for support in standard.support.all()
                        ],
                    )
                )
        except MultiValueDictKeyError:
            data = [dict(error="No page requested.")]
        finally:
            return JsonResponse(data=data, safe=False)
