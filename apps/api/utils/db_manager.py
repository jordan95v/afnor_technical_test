from dataclasses import dataclass
from datetime import datetime
from django.db.utils import IntegrityError
from apps.api.models import Standard, Support
from apps.api.utils.csv_manager import CSVRecord

__all__: list[str] = ["DBManager"]


@dataclass
class DBManager:
    async def insert(self, record: CSVRecord) -> None:
        """Insert the record into the database.

        Args:
            record: The record to insert, need to be an instance of CSVRecord.
        """
        standard: Standard
        try:
            standard = await Standard.objects.acreate(
                numdos=record.numdos,
                numdos_vl=record.numdos_vl,
                ancart=record.ancart,
                channel=record.channel,
                stage=record.stage,
                ve=record.ve,
            )
            print(
                f"[RECORD: {record.numdos}]"
                f"[TIMESTAMP: {datetime.now().strftime('%H:%M:%S')}] "
                f"Record {record.numdos} have been created."
            )
        except IntegrityError:
            print(
                f"[RECORD: {record.numdos}]"
                f"[TIMESTAMP: {datetime.now().strftime('%H:%M:%S')}] "
                f"Record {record.numdos} supports updated."
            )
            standard = await Standard.objects.aget(numdos=record.numdos)
        await self.create_support(standard=standard, support_format=record.format)

    async def create_support(self, standard: Standard, support_format: str) -> None:
        created: bool
        if support_format.isalpha():
            _, created = await Support.objects.aget_or_create(
                standard=standard, format=support_format
            )
            if created:
                print(
                    f"[RECORD: {support_format}]"
                    f"[TIMESTAMP: {datetime.now().strftime('%H:%M:%S')}] "
                    f"Record {standard.numdos} supports {support_format} created."
                )
            else:
                print(
                    f"[RECORD: {support_format}]"
                    f"[TIMESTAMP: {datetime.now().strftime('%H:%M:%S')}] "
                    f"Record {standard.numdos} supports {support_format} alredy exists."
                )
