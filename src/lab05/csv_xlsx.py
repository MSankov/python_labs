from openpyxl import Workbook
import csv
from pathlib import Path
from openpyxl.utils.cell import get_column_letter

def csv_to_xlsx(csv_path: str, xlsx_path: str) -> None:
    """
    Конвертирует CSV в XLSX.
    Использовать openpyxl ИЛИ xlsxwriter.
    Первая строка CSV — заголовок.
    Лист называется "Sheet1".
    Колонки — автоширина по длине текста (не менее 8 символов).
    """

    csv_p = Path(csv_path)
    xlsx_p = Path(xlsx_path)
    max_len = dict()
    MIN_LEN = 8

    wb = Workbook()
    ws = wb.active
    ws.title = "Sheet1"

    with open(csv_p, encoding="utf-8") as f:
        r = csv.reader(f)
        for row in r:
            for indx in range(len(row)):
                max_len[indx] = max(len(row[indx]),max_len.get(indx, MIN_LEN))
            ws.append(row)
        for indx in range(len(max_len)):
            ws.column_dimensions[get_column_letter(indx+1)].width = max_len[indx]
        wb.save(xlsx_p)

csv_to_xlsx('data/samples/cities.csv', 'data/out/people.xlsx')