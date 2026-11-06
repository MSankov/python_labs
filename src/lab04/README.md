## Лабораторная работа №4
  
**Задание A — модуль src/lab04/io_txt_csv.py**  
*Файл*: [io_txt_csv.py](io_txt_csv.py)  
*Ввод*: [test.py](test.py)
*Вывод*: тест кейсы
  
_Открывает файл на чтение в указанной кодировке и возвращает содержимое как одну строку_
![Демонстрация первой функции](/images/lab004/.......)
`read_text(path: str | Path, encoding: str = "utf-8") -> str` 
  
---
  
_Создает/перезаписывает CSV с разделителем_
![Демонстрация второй функции](/images/lab004/.......)
`write_csv(rows: list[tuple | list], path: str | Path, header: tuple[str, ...] | None = None) -> None` 

**Задание B — скрипт src/lab04/text_report.py**  
*Файл*: [text_report.py](text_report.py)  
*Ввод*: [test_report.py](test_report.py)
*Вывод*: тест кейсы
  
_Читает один входной файл data/input.txt, Нормализует текст (lib/text.py), токенизирует и считает частоты слов и сохраняет data/report.csv c колонками: (word,count), отсортированными: count ↓, слово ↑_
![Демонстрация программы](/images/lab004/.......)
`Пример запуска: python src/lab04/text_report.py` 
  
---  
  
**Star task — скрипт src/lab04/star_task.py**  
*Файл*: [star_task.py](star_task.py)  
*Ввод*: [test_report.py](test_report.py)
*Вывод*: тест кейсы
  
_Считает частоты по каждому файлу отдельно → data/report_per_file.csv со столбцами: (file,word,count) и формирует сводный отчёт по всем файлам вместе → data/report_total.csv_
![Демонстрация программы](/images/lab004/.......)
`Пример запуска: python src/lab04/text_report.py --in data/a.txt data/b.txt --per-file data/report_per_file.csv --total data/report_total.csv` 
  