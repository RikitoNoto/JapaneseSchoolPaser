from typing import Optional
from openpyxl.worksheet.worksheet import Worksheet
from openpyxl.cell.cell import Cell
from src.models.base_info import BaseInfo
from src.parser.parser import Parser


class BaseInfoParser(Parser):
    def parse(self) -> BaseInfo:
        """
        学校コードのセルを基準にデータを検索しパースする。
        """
        base_cell: Optional[Cell] = self._search_cell(
            "学校コード",
            self._sheet,
        )
        if not base_cell:
            raise ValueError("学校コードが見つかりませんでした。")
        return BaseInfo(
            school_code=self._sheet.cell(
                row=base_cell.row + 1, column=base_cell.column
            ).value,
            president=self._sheet.cell(
                row=base_cell.row + 1, column=base_cell.column + 1
            ).value,
        )
