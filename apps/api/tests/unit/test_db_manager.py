from re import A
from unittest.mock import MagicMock
import pytest
from pytest_mock import MockerFixture
from apps.api.models import Standard, Support
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

    async def test_support(self, mocker: MockerFixture):
        manager: DBManager = DBManager()
        spy: MagicMock = mocker.spy(Support.objects, "aget_or_create")
        standard: Standard = await Standard.objects.acreate(numdos="coucou")
        await manager.create_support(standard=standard, support_format="PDF")
        assert spy.call_count == 1
        await Standard.objects.filter(numdos="coucou").adelete()
        await Support.objects.all().adelete()

    async def test_support_already_exists(self):
        manager: DBManager = DBManager()
        standard: Standard = await Standard.objects.acreate(numdos="coucou")
        await Support.objects.acreate(standard=standard, format="PDF")
        await manager.create_support(standard=standard, support_format="PDF")
        supports: list[Support] = [support async for support in Support.objects.all()]
        assert len(supports) == 1

    async def test_insert_error(self, mocker: MockerFixture):
        manager: DBManager = DBManager()
        spy: MagicMock = mocker.spy(Standard.objects, "aget")
        await manager.insert(record=RECORD)
        await manager.insert(record=RECORD)
        assert spy.call_count == 1
