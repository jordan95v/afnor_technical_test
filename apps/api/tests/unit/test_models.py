from typing import Any
import pytest
from django.db.utils import IntegrityError
from apps.api.models import Standard
from conftest import STANDARD_DICT


@pytest.mark.asyncio
@pytest.mark.django_db
class TestStandard:
    async def test_init(self) -> None:
        await Standard.objects.acreate(**STANDARD_DICT)
        standard: Standard = await Standard.objects.alast()
        assert standard.numdos == "FA215012"
        assert standard.stage == 60.62
        await Standard.objects.filter(numdos=standard.numdos).adelete()

    async def test_fail(self) -> None:
        given: dict[str, Any] = dict(
            numdos=142,
            numdos_vl="FA215012",
            ancart="LNEN50289-1-3",
            channel="FRA",
            stage="hello",
            format="PDFC",
        )
        with pytest.raises(ValueError):
            await Standard.objects.acreate(**given)

    async def test_unique(self) -> None:
        await Standard.objects.acreate(**STANDARD_DICT)
        with pytest.raises(IntegrityError):
            await Standard.objects.acreate(**STANDARD_DICT)
