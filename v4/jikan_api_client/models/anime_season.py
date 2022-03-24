from enum import Enum


class AnimeSeason(str, Enum):
    SUMMER = "Summer"
    WINTER = "Winter"
    SPRING = "Spring"
    FALL = "Fall"

    def __str__(self) -> str:
        return str(self.value)
