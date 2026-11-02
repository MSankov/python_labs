from pathlib import Path
from typing import Iterable, Sequence
import csv
from src.libs.text import *

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

#print(read_text(r'data/lab04/input.txt'))
