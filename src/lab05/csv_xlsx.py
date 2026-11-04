from openpyxl import Workbook
import csv
from pathlib import Path
import csv

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

    wb = Workbook()
    ws = wb.active
    ws.title = "Sheet1"

    with open(csv_p, encoding="utf-8") as f:
        r = csv.reader(f)
        for row in r:
            ws.append(row)     
        wb.save(xlsx_p)

csv_to_xlsx('data/samples/people.csv', 'data/out/people.xlsx')