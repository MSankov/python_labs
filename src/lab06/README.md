## Лабораторная работа №6  
  
**CLI‑утилиты с argparse**  
  
**Задание А — Подкоманды в одном CLI**  
*Файл*: [cli_text.py](src/lab06/cli_text.py)  
  
_**Анализ частот слов в тексте (stats)**_  
Анализ частоты слов в тексте с использованием функций из `lab03`.  
![Демонстрация stats --help](images/lab06/stats_help.png)  
![Демонстрация stats выполнение](images/lab06/stats_run.png)  
`python src/lab06/cli_text.py stats --input data/samples/text.txt --top 5`  
`python src/lab06/cli_text.py stats --help`  
  
---  
  
_**Вывод содержимого файла (cat)**_  
Построчный вывод содержимого файла с возможностью нумерации строк.  
![Демонстрация cat --help](images/lab06/cat_help.png)  
![Демонстрация cat выполнение](images/lab06/cat_run.png)  
`python src/lab06/cli_text.py cat --input data/samples/text.txt -n`  
`python src/lab06/cli_text.py cat --help`  
  
---  
  
**Задание B — Конвертер форматов**  
*Файл*: [cli_convert.py](src/lab06/cli_convert.py)  
  
_**Перевести из json в csv**_  
![Демонстрация json2csv](images/lab06/json2csv.png)  
`python src/lab06/cli_convert.py json2csv --in data/samples/people.json --out data/out/people.csv`  
  
---  
  
_**Перевести из csv в json**_  
![Демонстрация csv2json](images/lab06/csv2json.png)  
`python src/lab06/cli_convert.py csv2json --in data/samples/people.csv --out data/out/people.json`  
  
---  
  
_**Перевести из csv в xlsx**_  
Конвертация с использованием функций из `lab05`.  
![Демонстрация csv2xlsx](images/lab06/csv2xlsx.png)  
`python src/lab06/cli_convert.py csv2xlsx --in data/samples/people.csv --out data/out/people.xlsx`  