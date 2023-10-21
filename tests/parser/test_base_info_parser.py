import openpyxl
from openpyxl.worksheet.worksheet import Worksheet
import os
import pytest
from src.models.base_info import BaseInfo
from src.parser.base_info_parser import BaseInfoParser


class TestBaseInfoParser:
    EXCEL_FILE_PATH_1 = f"{os.path.dirname(__file__)}/files/single_sheet_file1.xlsx"
    EXCEL_FILE_PATH_2 = f"{os.path.dirname(__file__)}/files/single_sheet_file2.xlsx"
    __book: openpyxl.Workbook

    @pytest.fixture
    def wrap(self):
        self.set_up()
        yield
        self.tear_down()

    def set_up(self):
        pass

    def tear_down(self):
        if self.__book:
            self.__book.close()

    def get_sheet(self, path) -> Worksheet:
        self.__book = openpyxl.load_workbook(path)
        return self.__book[self.__book.sheetnames[0]]

    def parse(self, path: str) -> BaseInfo:
        sheet = self.get_sheet(path)
        parser = BaseInfoParser(sheet)
        return parser.parse()

    @pytest.mark.parametrize(
        "path, expect",
        [
            (EXCEL_FILE_PATH_1, "F101110100010"),
            (EXCEL_FILE_PATH_2, "F123310106522"),
        ],
    )
    def test_should_parse_school_code(self, path: str, expect: str):
        base_info = self.parse(path)
        assert base_info.school_code == expect

    @pytest.mark.parametrize(
        "path, expect",
        [
            (EXCEL_FILE_PATH_1, "寳金 清博"),
            (EXCEL_FILE_PATH_2, "景山　節"),
        ],
    )
    def test_should_parse_president(self, path: str, expect: str):
        base_info = self.parse(path)
        assert base_info.president == expect
