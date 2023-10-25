from enum import Enum
from typing import Optional
from models.model import Model


class SchoolClassification(Enum):
    NATIONAL = "国立"
    PUBLIC = "公立"
    PRIVATE = "私立"

    @classmethod
    def from_str(cls, class_str: str):
        for value in list(cls):
            if value.value == class_str:
                return value


class BaseInfo(Model):
    def __init__(
        self, name="", school_code="", president="", classification=None
    ) -> None:
        self.__name = name
        self.__school_code: str = school_code
        self.__president: str = president
        self.__classification: Optional[SchoolClassification] = classification

    def _register_base_info(self, base_info):
        self.__name = base_info.name
        self.__school_code: str = base_info.school_code
        self.__president: str = base_info.president
        self.__classification: Optional[SchoolClassification] = base_info.classification

    @property
    def name(self) -> str:
        return self.__name

    @property
    def classification(self) -> SchoolClassification:
        return self.__classification

    @property
    def school_code(self) -> str:
        return self.__school_code

    @property
    def president(self) -> str:
        return self.__president
