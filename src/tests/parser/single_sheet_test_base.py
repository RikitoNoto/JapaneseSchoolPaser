from abc import ABC, abstractmethod
import openpyxl
from openpyxl.worksheet.worksheet import Worksheet
import os
import pytest
from typing import Generic, TypeVar

from parser.parser import Parser

T = TypeVar("T")


class SingleSheetTestBase(ABC, Generic[T]):
    EXCEL_FILE_PATH_1 = f"{os.path.dirname(__file__)}/files/single_sheet_file1.xlsx"
    EXCEL_FILE_PATH_2 = f"{os.path.dirname(__file__)}/files/single_sheet_file2.xlsx"
    EXCEL_FILE_PATH_3 = f"{os.path.dirname(__file__)}/files/single_sheet_file3.xlsx"
    __book: openpyxl.Workbook

    def setup_method(self, method):
        pass

    def teardown_method(self, method):
        if self.__book:
            self.__book.close()

    def get_sheet(self, path) -> Worksheet:
        self.__book = openpyxl.load_workbook(path)
        return self.__book[self.__book.sheetnames[0]]

    def parse(self, path: str) -> T:
        sheet = self.get_sheet(path)
        parser = self.get_parser(sheet)
        return parser.parse()

    @abstractmethod
    def get_parser(self, sheet: Worksheet) -> Parser:
        pass
