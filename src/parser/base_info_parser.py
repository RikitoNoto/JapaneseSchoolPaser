from typing import Optional
from openpyxl.worksheet.worksheet import Worksheet
from openpyxl.cell.cell import Cell
from src.models.base_info import BaseInfo


class BaseInfoParser:
    def __init__(self, sheet: Worksheet) -> None:
        self.__sheet = sheet

    def parse(self) -> BaseInfo:
        """
        学校コードのセルを基準にデータを検索しパースする。
        """
        base_cell: Optional[Cell] = self._search_cell(
            "学校コード",
            self.__sheet,
        )
        if not base_cell:
            raise ValueError("学校コードが見つかりませんでした。")
        return BaseInfo(
            school_code=self.__sheet.cell(
                row=base_cell.row + 1, column=base_cell.column
            ).value,
            president=self.__sheet.cell(
                row=base_cell.row + 1, column=base_cell.column + 1
            ).value,
        )

    def _search_cell(self, keyword: str, sheet: Worksheet) -> Optional[Cell]:
        """
        keywordをシートから検索し、最初に見つけたセルを返す。
        検索はA1→A2→B2→B1→A3→B3→C3→C2→C1
        のようにA1から(max_row, max_column)に直線を引くような方向で検索をする。

        Args:
            keyword (str): 検索するキーワード
            sheet (Worksheet): 検索対象のシート
        """

        for i in range(sheet.max_column):
            column = i + 1
            # columnを縦に検索
            for j in range(column - 1):
                row = i + 1
                column = j + 1
                if sheet.cell(row=row, column=column).value == keyword:
                    return sheet.cell(row=row, column=column)

            # rowとcolumnが同じセルを検索
            if sheet.cell(row=column, column=column).value == keyword:
                return sheet.cell(row=column, column=column)

            # rowを右から左に検索
            for j in reversed(range(column - 1)):
                row = j + 1
                if sheet.cell(row=row, column=column).value == keyword:
                    return sheet.cell(row=row, column=column)
