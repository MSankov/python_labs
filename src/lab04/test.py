from src.lab04.io_txt_csv import *
txt = read_text("data/lab04/input.txt")  # должен вернуть строку
print(txt)
write_csv([('sdfsd', 12), ('sdfdf', 1)], "data/lab04/check.csv", header=("word","count"))  # создаст CSV