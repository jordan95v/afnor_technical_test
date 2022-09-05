from typing import Any
import pytest
from apps.api.models import Standard


@pytest.mark.django_db
@pytest.mark.asyncio
class TestStandard:
    async def test_init(self):
        given: dict[str, Any] = dict(
            numdos="FA215012",
            numdos_vl="FA215012",
            ancart="LNEN50289-1-3",
            channel="FRA",
            stage=60.62,
            format="PDFC",
        )
        await Standard.objects.acreate(**given)
        standard: Standard = await Standard.objects.afirst()
        assert standard.numdos == "FA215012"
        assert standard.stage == 60.62
