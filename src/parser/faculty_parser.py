from typing import Optional
from openpyxl.worksheet.worksheet import Worksheet
from openpyxl.cell.cell import Cell
from src.models.faculty import Faculty
from src.parser.parser import Parser


class FacultyParser(Parser):
    def parse(self) -> list[Faculty]:
        """
        学部のセルを基準にデータを検索しパースする。
        """
        base_cell: Optional[Cell] = self._search_cell(
            "学部",
            self._sheet,
        )
        if not base_cell:
            raise ValueError('"学部"の文字が見つかりませんでした。')

        row = base_cell.row + 3  # 学部の3行下から開始
        column = base_cell.column
        faculties: list[Faculty] = []
        # 空白のセルが見つかるまで、下を検索
        while self._sheet.cell(row=row, column=column).value not in [None, ""]:
            faculty = self._sheet.cell(row=row, column=column).value

            # 初めて見つけた学科の場合は新規追加
            if faculty not in [f.name for f in faculties]:
                faculties.append(
                    Faculty(self._sheet.cell(row=row, column=column).value)
                )
            row += 1

        return faculties
