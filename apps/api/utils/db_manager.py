from dataclasses import dataclass
from datetime import datetime
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
        standard = await Standard.objects.aget(numdos=record.numdos)
        if standard:
            print(
                f"[RECORD: {record.numdos}]"
                f"[TIMESTAMP: {datetime.now().strftime('%H:%M:%S')}] "
                f"Record {record.numdos} already exists."
            )
        else:
            print(
                f"[RECORD: {record.numdos}]"
                f"[TIMESTAMP: {datetime.now().strftime('%H:%M:%S')}] "
                f"Record {record.numdos} have been created."
            )
            standard = Standard.objects.acreate(
                numdos=record.numdos,
                numdos_vl=record.numdos_vl,
                ancart=record.ancart,
                channel=record.channel,
                stage=record.stage,
                ve=record.ve,
            )
        await Support.objects.acreate(standard=standard, format=record.format)
