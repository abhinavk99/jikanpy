from enum import Enum


class GetSchedulesFilter(str, Enum):
    MONDAY = "monday"
    TUESDAY = "tuesday"
    WEDNESDAY = "wednesday"
    THURSDAY = "thursday"
    FRIDAY = "friday"
    UNKNOWN = "unknown"
    OTHER = "other"

    def __str__(self) -> str:
        return str(self.value)
