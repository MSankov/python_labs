from src.libs.text import *
from pathlib import Path
from src.lab04.io_txt_csv import *

files = sorted(Path(r'data/lab04').glob('?.txt'))
rows = list()

total_w = list()

for p in files:
    if not p.is_file():
        continue
    print(f'Обработка файла {p.name}')
    data = read_text(path=p)
    data = normalize(data)
    w = tokenize(data)
    total_w.extend(w)
    sl = count_freq(w)
    for el in list(sl.items()):
        rows.append((p.name, el[0], el[1]))

write_csv(rows,'data/lab04/report_per_file.csv',('file','word','count'))
print('Отчет по файлам сохранен в data/lab04/report_per_file.csv')

sl = count_freq(total_w)
write_csv(list(sl.items()),'data/lab04/report_total.csv',('word','count'))
print('Общий отчет сохранен в data/lab04/report_total.csv')