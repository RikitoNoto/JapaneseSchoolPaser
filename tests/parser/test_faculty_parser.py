from openpyxl.worksheet.worksheet import Worksheet
import pytest
from src.models.faculty import Faculty
from src.parser.faculty_parser import FacultyParser
from src.parser.parser import Parser
from tests.parser.single_sheet_test_base import SingleSheetTestBase


class TestFacultyParser(SingleSheetTestBase[list[Faculty]]):
    def get_parser(self, sheet: Worksheet) -> Parser:
        return FacultyParser(sheet)

    @pytest.mark.parametrize(
        "path, exp",
        [
            (
                SingleSheetTestBase.EXCEL_FILE_PATH_1,
                [
                    "文学部",
                    "教育学部",
                    "法学部",
                    "経済学部",
                    "理学部",
                    "医学部",
                    "歯学部",
                    "薬学部",
                    "工学部",
                    "農学部",
                    "獣医学部",
                    "水産学部",
                ],
            ),
            (
                SingleSheetTestBase.EXCEL_FILE_PATH_2,
                [
                    "情報メディア学部",
                    "健康生活学部",
                ],
            ),
        ],
    )
    def test_should_parse_faculty(self, path: str, exp: list[str]):
        faculties = self.parse(path)
        for faculty in faculties:
            assert faculty.name in exp
            exp.remove(faculty.name)
