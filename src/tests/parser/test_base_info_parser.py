from openpyxl.worksheet.worksheet import Worksheet
import pytest
from models.base_info import BaseInfo
from parser.base_info_parser import BaseInfoParser
from parser.parser import Parser
from tests.parser.single_sheet_test_base import SingleSheetTestBase


class TestBaseInfoParser(SingleSheetTestBase[BaseInfo]):
    def get_parser(self, sheet: Worksheet) -> Parser:
        return BaseInfoParser(sheet)

    @pytest.mark.parametrize(
        "path, exp",
        [
            (SingleSheetTestBase.EXCEL_FILE_PATH_1, "F101110100010"),
            (SingleSheetTestBase.EXCEL_FILE_PATH_2, "F123310106522"),
        ],
    )
    def test_should_parse_school_code(self, path: str, exp: str):
        base_info = self.parse(path)
        assert base_info.school_code == exp

    @pytest.mark.parametrize(
        "path, exp",
        [
            (SingleSheetTestBase.EXCEL_FILE_PATH_1, "寳金 清博"),
            (SingleSheetTestBase.EXCEL_FILE_PATH_2, "景山　節"),
        ],
    )
    def test_should_parse_president(self, path: str, exp: str):
        base_info = self.parse(path)
        assert base_info.president == exp

    @pytest.mark.parametrize(
        "path, exp",
        [
            (SingleSheetTestBase.EXCEL_FILE_PATH_1, "北海道大学"),
            (SingleSheetTestBase.EXCEL_FILE_PATH_2, "名古屋文理大学"),
        ],
    )
    def test_should_parse_school_name(self, path: str, exp: str):
        base_info = self.parse(path)
        assert base_info.name == exp
