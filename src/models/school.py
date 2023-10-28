from typing import Optional
from models.base_info import BaseInfo
from models.faculty import Faculty
from models.graduate_school import GraduateSchool


class School(BaseInfo):
    def __init__(
        self,
        base_info: Optional[BaseInfo] = None,
        faculties: list[Faculty] = [],
        graduate_schools: list[GraduateSchool] = [],
        **kwargs,
    ) -> None:
        self.__faculties = faculties
        self.__graduate_schools = graduate_schools
        if base_info:
            self._register_base_info(base_info)
        else:
            super().__init__(**kwargs)

    @property
    def faculties(self) -> list[Faculty]:
        return self.__faculties

    @property
    def graduate_schools(self) -> list[GraduateSchool]:
        return self.__graduate_schools
