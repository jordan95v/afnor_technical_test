from pathlib import Path
from typing import Any
import pytest
from apps.api.utils.csv_manager import CSVManager, CSVRecord


class TestCSVRecord:
    def test_init(self) -> None:
        record: CSVRecord = CSVRecord(
            numdos="hello",
            numdos_vl="my",
            ancart="name",
            channel="is",
            stage="50",
            ve="cents",
            format="yo",
        )
        assert isinstance(record, CSVRecord)
        assert record.numdos == "hello"

    def test_as_dict(self):
        record: CSVRecord = CSVRecord(
            numdos="hello",
            numdos_vl="my",
            ancart="name",
            channel="is",
            stage="50",
            ve="cents",
            format="yo",
        )
        assert isinstance(record.as_dict(), dict)


@pytest.mark.asyncio
class TestCSVManager:
    csv_file: Path = Path("apps/api/tests/samples/obfuscated_source.csv")

    async def test_read(self) -> None:
        manager: CSVManager = CSVManager()
        res: list[CSVRecord] = await manager.read_csv(file=self.csv_file)
        assert res[0].numdos == "DD237051"

    async def test_create_record(self):
        manager: CSVManager = CSVManager()
        given: dict[str, Any] = {
            "NUMDOS": "HA630006",
            "NUMDOSVERLING": "HA630006",
            "ANCART": "P82472",
            "FILIERE": "FRA",
            "ETAPE": "99.60",
            "VERLING": "F",
            "FORMAT": "",
        }
        res: CSVRecord = await manager._create(given)
        assert res.numdos == "HA630006"
        assert res.stage == "99.60"
