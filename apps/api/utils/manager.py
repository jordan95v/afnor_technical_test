import asyncio
import csv
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Any, Iterator

__all__: list[str] = ["CSVRecord", "CSVManager"]


@dataclass
class CSVRecord:
    numdos: str | None = None
    numdos_vl: str | None = None
    ancart: str | None = None
    channel: str | None = None
    stage: str | None = None
    ve: str | None = None
    format: str | None = None

    def as_dict(self):
        return asdict(self)


@dataclass
class CSVManager:
    async def _create(self, record: dict[str, Any]) -> CSVRecord:
        """Create a CSVRecord object.

        Args:
            record: Dict needed to create the object.

        Return:
            CSVRecord: The object created
        """

        return CSVRecord(*record.values())

    async def read_csv(self, file: Path) -> list[CSVRecord]:
        """Read a CSF file.

        Args:
            file: Path to the CSV file.

        Return:
            list[CSVRecord]: List of CSVRecord created using the CSV file.
        """

        reader: csv.DictReader = csv.DictReader(
            file.open(encoding="utf8"), delimiter="|"
        )
        return await asyncio.gather(*[self._create(element) for element in reader])
