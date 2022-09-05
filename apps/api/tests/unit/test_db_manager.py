import pytest
from django.db.utils import IntegrityError
from apps.api.models import Standard
from apps.api.utils.db_manager import DBManager
from conftest import RECORD


@pytest.mark.asyncio
@pytest.mark.django_db
class TestDBManager:
    async def test_insert(self) -> None:
        manager: DBManager = DBManager()
        await manager.insert(record=RECORD)
        res: Standard = await Standard.objects.alast()
        assert res.numdos == "hello"
        await Standard.objects.filter(numdos=RECORD.numdos).adelete()
