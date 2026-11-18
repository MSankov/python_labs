import argparse
from src.libs.text import *
from pathlib import Path

def main():
    parser = argparse.ArgumentParser(description="CLI‑утилиты лабораторной №6")
    subparsers = parser.add_subparsers(dest="command")

    # подкоманда cat
    cat_parser = subparsers.add_parser("cat", help="Вывести содержимое файла")
    cat_parser.add_argument("--input", required=True, help="Путь к файлу")
    cat_parser.add_argument("-n", action="store_true", help="Нумеровать строки")

    # подкоманда stats
    stats_parser = subparsers.add_parser("stats", help="Частоты слов")
    stats_parser.add_argument("--input", required=True)
    stats_parser.add_argument("--top", type=int, default=5)

    args = parser.parse_args()

    if args.command == "cat":
        s = read_text(Path(args.input))
        m = s.split('\n')
        if args.n is not None:
            for n in range(len(m)):
                print(f'{n+1}) {m[n]}')
        else:
            for el in m:
                print(el)

        
    elif args.command == "stats":
        s = read_text(Path(args.input))
        s = normalize()
        l = tokenize(s)
        l = count_freq(l)
        print(top_n(l))

        