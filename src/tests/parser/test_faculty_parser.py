from openpyxl.worksheet.worksheet import Worksheet
import pytest
from models.faculty import Faculty
from parser.faculty_parser import FacultyParser
from parser.parser import Parser
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

    @pytest.mark.parametrize(
        "path, exp",
        [
            (
                SingleSheetTestBase.EXCEL_FILE_PATH_1,
                {
                    "文学部": [
                        "人文科学科",
                    ],
                    "教育学部": [
                        "教育学科",
                    ],
                    "法学部": [
                        "法学課程",
                    ],
                    "経済学部": [
                        "経済学科",
                        "経営学科",
                    ],
                    "理学部": [
                        "数学科",
                        "物理学科",
                        "化学科",
                        "生物科学科",
                        "地球惑星科学科",
                    ],
                    "医学部": [
                        "医学科",
                        "保健学科",
                    ],
                    "歯学部": [
                        "歯学科",
                    ],
                    "薬学部": [
                        "薬科学科",
                        "薬学科",
                    ],
                    "工学部": [
                        "応用理工系学科",
                        "情報エレクトロニクス学科",
                        "機械知能工学科",
                        "環境社会工学科",
                        "（共通）",
                    ],
                    "農学部": [
                        "生物資源科学科",
                        "応用生命科学科",
                        "生物機能化学科",
                        "森林科学科",
                        "畜産科学科",
                        "生物環境工学科",
                        "農業経済学科",
                    ],
                    "獣医学部": [
                        "共同獣医学課程",
                    ],
                    "水産学部": [
                        "海洋生物科学科",
                        "海洋資源科学科",
                        "増殖生命科学科",
                        "資源機能化学科",
                    ],
                },
            ),
            (
                SingleSheetTestBase.EXCEL_FILE_PATH_2,
                {
                    "情報メディア学部": [
                        "情報メディア学科",
                    ],
                    "健康生活学部": [
                        "健康栄養学科",
                        "フードビジネス学科",
                    ],
                },
            ),
        ],
    )
    def test_should_parse_departments(self, path: str, exp: dict[str, list[str]]):
        faculties = self.parse(path)
        for faculty in faculties:
            exp_departments: list[str] = exp[faculty.name]
            assert len(exp_departments) == len(faculty.departments)
            for department in faculty.departments:
                assert department.name in exp_departments
                exp_departments.remove(department.name)
