from src.libs.text import *
from pathlib import Path
from src.lab04.io_txt_csv import *



data = read_text('data/lab04/input.txt')
data = normalize(data)
w = tokenize(data)
sl = count_freq(w)
top = top_n(sl, n = 5)


write_csv(list(sl.items()),'data/lab04/report.csv',('word','count'))
print(f'Всего слов: {len(w)}')
print(f'Уникальных слов: {len(sl)}')
print(f'Топ-5: {print_table(top)}')