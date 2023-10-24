from openpyxl.worksheet.worksheet import Worksheet
import pytest
from models.graduate_school import GraduateSchool
from parser.graduate_school_parser import GraduateSchoolParser
from parser.parser import Parser
from tests.parser.single_sheet_test_base import SingleSheetTestBase


class TestGraduateSchoolParser(SingleSheetTestBase[list[GraduateSchool]]):
    def get_parser(self, sheet: Worksheet) -> Parser:
        return GraduateSchoolParser(sheet)

    @pytest.mark.parametrize(
        "path, exp",
        [
            (
                SingleSheetTestBase.EXCEL_FILE_PATH_1,
                [
                    "法学研究科",
                    "水産科学院",
                    "環境科学院",
                    "理学院",
                    "農学院",
                    "生命科学院",
                    "教育学院",
                    "国際広報メディア・観光学院",
                    "保健科学院",
                    "工学院",
                    "総合化学院",
                    "経済学院",
                    "医学院",
                    "歯学院",
                    "獣医学院",
                    "医理工学院",
                    "国際感染症学院",
                    "国際食資源学院",
                    "文学院",
                    "情報科学院",
                    "公共政策学教育部",
                ],
            ),
            (
                SingleSheetTestBase.EXCEL_FILE_PATH_2,
                [],
            ),
        ],
    )
    def test_should_parse_graduate_school(self, path: str, exp: list[str]):
        graduate_schools = self.parse(path)
        assert len(graduate_schools) == len(exp)
        for graduate_school in graduate_schools:
            assert graduate_school.name in exp
            exp.remove(graduate_school.name)

    @pytest.mark.parametrize(
        "path, exp",
        [
            (
                SingleSheetTestBase.EXCEL_FILE_PATH_1,
                {
                    "法学研究科": [
                        "法学政治学専攻",
                        "法律実務専攻",
                    ],
                    "水産科学院": [
                        "海洋生物資源科学専攻",
                        "海洋応用生命科学専攻",
                    ],
                    "環境科学院": [
                        "環境起学専攻",
                        "地球圏科学専攻",
                        "生物圏科学専攻",
                        "環境物質科学専攻",
                    ],
                    "理学院": [
                        "数学専攻",
                        "物性物理学専攻",
                        "宇宙理学専攻",
                        "自然史科学専攻",
                    ],
                    "農学院": [
                        "農学専攻",
                    ],
                    "生命科学院": [
                        "生命科学専攻",
                        "臨床薬学専攻",
                        "ソフトマター専攻",
                    ],
                    "教育学院": [
                        "教育学専攻",
                    ],
                    "国際広報メディア・観光学院": [
                        "国際広報メディア・観光学専攻",
                    ],
                    "保健科学院": [
                        "保健科学専攻",
                    ],
                    "工学院": [
                        "応用物理学専攻",
                        "材料科学専攻",
                        "機械宇宙工学専攻",
                        "人間機械システムデザイン専攻",
                        "エネルギー環境システム専攻",
                        "量子理工学専攻",
                        "環境フィールド工学専攻",
                        "北方圏環境政策工学専攻",
                        "建築都市空間デザイン専攻",
                        "空間性能システム専攻",
                        "環境創生工学専攻",
                        "環境循環システム専攻",
                        "共同資源工学専攻",
                    ],
                    "総合化学院": [
                        "総合化学専攻",
                    ],
                    "経済学院": [
                        "現代経済経営専攻",
                        "会計情報専攻",
                    ],
                    "医学院": [
                        "医科学専攻",
                        "医学専攻",
                    ],
                    "歯学院": [
                        "口腔医学専攻",
                    ],
                    "獣医学院": [
                        "獣医学専攻",
                    ],
                    "医理工学院": [
                        "医理工学専攻",
                    ],
                    "国際感染症学院": [
                        "感染症学専攻",
                    ],
                    "国際食資源学院": [
                        "国際食資源学専攻",
                    ],
                    "文学院": [
                        "人文学専攻",
                        "人間科学専攻",
                    ],
                    "情報科学院": [
                        "情報科学専攻",
                    ],
                    "公共政策学教育部": [
                        "公共政策学専攻",
                    ],
                },
            ),
            (
                SingleSheetTestBase.EXCEL_FILE_PATH_2,
                {},
            ),
        ],
    )
    def test_should_parse_departments(self, path: str, exp: dict[str, list[str]]):
        graduate_schools = self.parse(path)
        for graduate_school in graduate_schools:
            exp_graduate_schools: list[str] = exp[graduate_school.name]
            assert len(exp_graduate_schools) == len(graduate_school.majors)
            for major in graduate_school.majors:
                assert major.name in exp_graduate_schools
                exp_graduate_schools.remove(major.name)
