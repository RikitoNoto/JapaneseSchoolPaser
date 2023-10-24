from typing import Optional
from openpyxl.cell.cell import Cell
from models.base_info import BaseInfo
from models.faculty import Faculty
from models.graduate_school import GraduateSchool
from models.school import School
from parser.parser import Parser
from parser.base_info_parser import BaseInfoParser
from parser.faculty_parser import FacultyParser
from parser.graduate_school_parser import GraduateSchoolParser


class SchoolParser(Parser):
    def parse(self) -> BaseInfo:
        """
        シートから学校をパースする
        """
        base_info: BaseInfo = BaseInfoParser(self._sheet).parse()
        faculties: list[Faculty] = FacultyParser(self._sheet).parse()
        graduate_schools: list[GraduateSchool] = GraduateSchoolParser(
            self._sheet
        ).parse()

        return School(
            school_code=base_info.school_code,
            president=base_info.president,
            faculties=faculties,
            graduate_schools=graduate_schools,
        )
