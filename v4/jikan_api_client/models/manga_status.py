from enum import Enum


class MangaStatus(str, Enum):
    FINISHED = "Finished"
    PUBLISHING = "Publishing"
    ON_HIATUS = "On Hiatus"
    DISCONTINUED = "Discontinued"
    NOT_YET_PUBLISHED = "Not yet published"

    def __str__(self) -> str:
        return str(self.value)
