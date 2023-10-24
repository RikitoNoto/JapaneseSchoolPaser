from typing import Any

from openpyxl import load_workbook
from openpyxl.workbook import Workbook
from openpyxl.worksheet.worksheet import Worksheet

from src.models.school import School
from src.parser.school_parser import SchoolParser


def parse_schools_to_dict(path: str) -> dict[str, Any]:
    pass


def parse_schools_to_model(path: str) -> list[School]:
    book: Workbook = load_workbook(path)
    schools: list[School] = []

    sheet_names = book.sheetnames
    for sheet_name in sheet_names:
        sheet: Worksheet = book[sheet_name]
        schools.append(SchoolParser(sheet).parse())

    book.close()

    return schools
