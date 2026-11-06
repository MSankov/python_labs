## Лабораторная работа №5
  
**Задание A — JSON ↔ CSV**  
*Файл*: [json_csv.py](json_csv.py)  
*Ввод*: {name1}.json / {name1}.csv
*Вывод*: {name2}.csv / {name2}.json
  
_Перевести из json в csv_
![Демонстрация первой функции](/images/lab05/json1.png)  
![Демонстрация первой функции](/images/lab05/csv1.png)    
`json_to_csv('data/samples/people.json', 'data/out/people_from_json.csv')`  
  
  
---
  
_Перевести из csv в json_  
![Демонстрация второй функции](/images/lab05/csv2.png)  
![Демонстрация первой функции](/images/lab05/json2.png)    
`csv_to_json('data/samples/people.csv', 'data/out/people_from_csv.json')`  
  

**Задание B — CSV → XLSX**  
*Файл*: [csv_xlsx.py](csv_xlsx.py)  
*Ввод*: {name1}.csv
*Вывод*: {name2}.xlsx
  
_Перевести из csv в xlsx_  
![Демонстрация второй функции](/images/lab05/csv3.png)  
![Демонстрация первой функции](/images/lab05/xlsx3.png)    
`csv_to_xlsx('data/samples/people.csv', 'data/out/people.xlsx')`  