from dataclasses import dataclass
from datetime import datetime
from django.db.utils import IntegrityError
from apps.api.models import Standard
from apps.api.utils.csv_manager import CSVRecord


@dataclass
class DBManager:
    async def insert(self, record: CSVRecord) -> None:
        """Insert the record into the database.

        Args:
            record: The record to insert, need to be an instance of CSVRecord.
        """

        try:
            await Standard.objects.acreate(**record.as_dict())
        except IntegrityError:
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
