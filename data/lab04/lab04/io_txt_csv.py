from pathlib import Path
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
    s = ''
    with open(path, encoding="utf-8") as f:
        for line in f:
            s += line.rstrip("\n")
    return s

import csv
from pathlib import Path
from typing import Iterable, Sequence

def write_csv(rows: Iterable[Sequence], path: str | Path,
              header: tuple[str, ...] | None = None) -> None:
    for i in range(len(rows)):
        if len(rows[i]) != len(rows[i+1]):
            raise ValueError('в атрибуте rows строки имеют разные длины')
    p = Path(path)
    rows = list(rows)
    with p.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if header is not None:
            w.writerow(header)
        for r in rows:
            w.writerow(r)
    f = f.replace(';',',')



print(read_text('/Users/Михаил/Downloads/9_12.csv'))
