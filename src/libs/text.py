import re
from pathlib import Path
from typing import Iterable, Sequence
import csv
from openpyxl import Workbook
from openpyxl.utils.cell import get_column_letter
import json

def normalize(text: str, *, casefold: bool = True, yo2e: bool = True):
    '''Убирает невидимые управляющие символы (например, \t, \r) → заменяет на пробелы,
        схлопывает повторяющиеся пробелы в один.
    
        Args:
            text: str, 
            casefold: bool = True, (Если casefold=True — привести к casefold. Если casefold=False - используем lower().)
            yo2e: bool = True (Если yo2e=True — заменить все ё/Ё на е/Е.)
        
        Returns:
            str
    
        Raises:
        '''
    
    if casefold:
        text = text.casefold()
    else:
        text = text.lower()

    if yo2e:
        text = text.replace('ё', 'е')

    text = " ".join(text.split())
    return text

def tokenize(text: str):
    '''Разбить на «слова» по небуквенно-цифровым разделителям.
    
        Args:
            text: str
        
        Returns:
            list[str]
    '''
    res = re.findall(r"\w+(?:-\w+)*",text)
    return res

def count_freq(tokens: list[str]):
    '''Подсчитать частоты, вернуть словарь слово → количество.
    
        Args:
            list[str]
        
        Returns:
            dict[str, int]
    '''
    res = {}
    for s in tokens:
        if s in res:
            res[s]+=1
        else:
            res[s] = 1
    return res

def top_n(freq: dict[str, int], n: int = 5):
    '''Вернуть топ-N по убыванию частоты; при равенстве — по алфавиту слова.
    
    Args:
        list[str]
        
    Returns:
        list[tuple[str, int]]
    '''
    res = []
    items = list(freq.items())
    #dict_items([('a', 3), ('b', 2), ('c', 1)])
    for i in range(len(items)-1):
        for j in range(i+1, len(items)):
            if items[j][1] > items[i][1]:
                (items[i], items[j]) = (items[j], items[i])
            elif items[j][1] == items[i][1] and items[j][0] < items[i][0]:
                (items[i], items[j]) = (items[j], items[i])

    return items[:n]

def print_table(data: dict[str, int]):
    max_len = 5
    for el in data:
        if len(el[0]) > max_len:
            max_len = len(el[0])

    print(f'{'слово':{max_len}} | частота')
    print('-'*(max_len+12))
    for el in data:
        print(f'{el[0]:{max_len}} | {el[1]:^7}')


def read_text(path: str | Path, encoding: str = "utf-8"):

    '''Открывает файл на чтение в указанной кодировке и возвращает содержимое как одну строку.
        
        Args:
            str | Path
            
        Returns:
            str
        
        Raises:
            FileNotFoundError - если файл не найден
            UnicodeDecodeError  - если кодировка не подходит
            '''
    
    p = Path(path)
    return p.read_text(encoding=encoding).replace('\n',' ')



def write_csv(rows: Iterable[Sequence], path: str | Path,
              header: tuple[str, ...] | None = None) -> None:
    '''
    Создает/перезаписывает CSV с разделителем ,
    '''
    p = Path(path)
    rows = list(rows) 

    for i in range(len(rows)):
        if len(rows[0]) != len(rows[i]):
            raise ValueError('в атрибуте rows строки имеют разные длины')

    with p.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f, delimiter=',')
        if header is not None:
            w.writerow(header)
        for r in rows:
            w.writerow(r)


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



def json_to_csv(json_path: str, csv_path: str) -> None:
    """
    Преобразует JSON-файл в CSV.
    Поддерживает список словарей [{...}, {...}], заполняет отсутствующие поля пустыми строками.
    Кодировка UTF-8. Порядок колонок — как в первом объекте или алфавитный (указать в README).
    """
    json_p = Path(json_path)
    csv_p = Path(csv_path)
    with json_p.open('r', encoding="utf-8") as f:
        data = json.load(f)

    header = set()
    for el in data:
        header = header | el.keys()



    with csv_p.open('w', newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames = header)
        writer.writeheader()
        writer.writerows(data)



def csv_to_json(csv_path: str, json_path: str) -> None:
    """
    Преобразует CSV в JSON (список словарей).
    Заголовок обязателен, значения сохраняются как строки.
    json.dump(..., ensure_ascii=False, indent=2)
    """
    csv_p = Path(csv_path)
    json_p = Path(json_path)

    with open(csv_path, encoding="utf-8") as f:
        r = csv.DictReader(f)
        data = list(r)
    

    with json_p.open("w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent='\t')
