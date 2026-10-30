from src.libs.text import *
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
    with open(path, encoding="utf-8") as f:
        f = normalize(f)
        f = tokenize(f)
        sl = count_freq(f)
        top = top_n(sl, n = 5)
    return len(f), len(sl), top 
    
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

write_csv(sl,'data/report.csv',('word','count'))
s = read_text('data/input.txt')
print(f'Всего слов: {s[0]}')
print(f'Уникальных слов: {s[1]}')
print(f'Топ-5: {list(s[2])}')