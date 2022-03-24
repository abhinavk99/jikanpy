from enum import Enum


class UsersSearchQueryGender(str, Enum):
    ANY = "any"
    MALE = "male"
    FEMALE = "female"
    NONBINARY = "nonbinary"

    def __str__(self) -> str:
        return str(self.value)
