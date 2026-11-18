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
        path = Path(args.input)
        text = read_text(path)
        lines = text.splitlines()
        if args.n:
            for i, line in enumerate(lines, start=1):
                print(f"{i:>4}  {line}")
        else:
            for line in lines:
                print(line)

        
    elif args.command == "stats":
        path = Path(args.input)
        text = read_text(path)
        norm_text = normalize(text)
        tokens = tokenize(norm_text)
        freq = count_freq(tokens)
        top_words = top_n(freq, args.top)
        print(f"Топ-{args.top} слов:")
        for word, count in top_words:
            print(f"{word}: {count}")

if __name__ == "__main__":
    main()