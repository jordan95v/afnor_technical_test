import asyncio
from pathlib import Path
from typing import Any
from django.core.management.base import BaseCommand, CommandParser
from apps.api.utils.csv_manager import CSVManager, CSVRecord
from apps.api.utils.db_manager import DBManager


class Command(BaseCommand):
    async def insert_db(self, file: Path):
        csv_manager: CSVManager = CSVManager()
        db_manager: DBManager = DBManager()
        records: list[CSVRecord] = await csv_manager.read_csv(file=file)
        await asyncio.gather(*[db_manager.insert(record) for record in records])

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument(
            "--csv", type=Path, help="Indicates the path to the csv file."
        )

    def handle(self, *args: Any, **kwargs: Any) -> None:
        asyncio.run(self.insert_db(file=kwargs["csv"]))
