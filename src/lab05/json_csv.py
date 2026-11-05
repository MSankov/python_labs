import json
from pathlib import Path
import csv


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


json_to_csv('data/samples/people.json', 'data/out/people_from_json.csv')


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

csv_to_json('data/samples/people.csv', 'data/out/people_from_csv.json')
