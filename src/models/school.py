from models.base_info import BaseInfo
from models.faculty import Faculty
from models.graduate_school import GraduateSchool


class School(BaseInfo):
    def __init__(
        self,
        school_code="",
        president="",
        faculties: list[Faculty] = [],
        graduate_schools: list[GraduateSchool] = [],
    ) -> None:
        self.__faculties = faculties
        self.__graduate_schools = graduate_schools
        super().__init__(school_code, president)

    @property
    def faculties(self) -> list[Faculty]:
        return self.__faculties

    @property
    def graduate_schools(self) -> list[GraduateSchool]:
        return self.__graduate_schools
