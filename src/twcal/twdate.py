from dataclasses import dataclass

from twcal.constants import MINGUO_BEFORE_DATE_FORMAT, MINGUO_DATE_FORMAT
from twcal.utils import validate_minguo_date


@dataclass(order=True)
class TWDate:
    """Represent a date in the Minguo (ROC) calendar system."""

    year: int
    month: int
    day: int

    def __post_init__(self):
        """Validate the Minguo date upon creation."""
        validate_minguo_date(self.year, self.month, self.day)

    def __str__(self) -> str:
        """Return the date as a full Minguo string, e.g. '民國115年3月20日'."""
        return self.to_string()

    @classmethod
    def from_short_string(cls, s: str) -> "TWDate":
        """Parse a compact numeric string, e.g. '1150320', into a TWDate."""
        day = int(s[-2:])
        month = int(s[-4:-2])
        year = int(s[:-4])
        return cls(year, month, day)

    def to_string(self) -> str:
        """Return the date as a full Minguo string, e.g. '民國115年3月20日'."""
        if self.year < 0:
            return MINGUO_BEFORE_DATE_FORMAT.format(
                year=abs(self.year), month=self.month, day=self.day
            )
        return MINGUO_DATE_FORMAT.format(
            year=self.year, month=self.month, day=self.day
        )

    def to_short_string(self) -> str:
        """Return the date as a compact numeric string, e.g. '1150320'."""
        return f"{self.year}{self.month:02d}{self.day:02d}"
