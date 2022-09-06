from typing import Any

from apps.api.utils.csv_manager import CSVRecord


STANDARD_DICT: dict[str, Any] = dict(
    numdos="FA215012",
    numdos_vl="FA215012",
    ancart="LNEN50289-1-3",
    channel="FRA",
    stage=60.62,
)

RECORD: CSVRecord = CSVRecord(
    numdos="hello",
    numdos_vl="my",
    ancart="name",
    channel="is",
    stage="50",
    ve="cents",
    format="yo",
)
