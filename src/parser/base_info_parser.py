from typing import Optional
from openpyxl.cell.cell import Cell
from models.base_info import BaseInfo
from parser.parser import Parser


class BaseInfoParser(Parser):
    def parse(self) -> BaseInfo:
        """
        学校コードのセルを基準にデータを検索しパースする。
        それに加えて、ファイル名とB1セルから大学名と学校タイプをパースする。
        学校コードが見つからない場合は、情報が取得できないためValueErrorをraiseする。
        """
        base_cell: Optional[Cell] = self._search_cell(
            "学校コード",
            self._sheet,
        )
        if not base_cell:
            raise ValueError("学校コードが見つかりませんでした。")

        name = self._sheet.title  # シート名が大学名

        return BaseInfo(
            name=name,
            school_code=self._sheet.cell(
                row=base_cell.row + 1, column=base_cell.column
            ).value,
            president=self._sheet.cell(
                row=base_cell.row + 1, column=base_cell.column + 1
            ).value,
        )
