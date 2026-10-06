from src.libs.text import *
''''ПрИвЕт\nМИр\t" → "привет мир" (casefold + схлопнуть пробелы)
"ёжик, Ёлка" (yo2e=True) → "ежик, елка"
"Hello\r\nWorld" → "hello world"
"  двойные   пробелы  " → "двойные пробелы"'''

'''print(normalize("ПрИвЕт\nМИр\t"))
print(normalize("ёжик, Ёлка", yo2e=True))
print(normalize("Hello\r\nWorld"))
print(normalize("  двойные   пробелы  "))'''

'''print(tokenize("привет мир"))
print(tokenize("hello,world!!!"))
print(tokenize("по--настоящему круто"))
print(tokenize("доброта - это хорошо"))
print(tokenize("emoji 😀 не слово"))'''


'''"привет мир" → ["привет", "мир"]
"hello,world!!!" → ["hello", "world"]
"по-настоящему круто" → ["по-настоящему", "круто"]
"2025 год" → ["2025", "год"]
"emoji 😀 не слово" → ["emoji", "не", "слово"] (эмодзи выпадают)'''


#print(count_freq(["a","b","a","c","b","a"]))
print(top_n({"aa":2,"bb":2,"cc":1}, n=2))
'''

data = "Привет, мир! Привет!!!"
data = normalize(data)
tokens = tokenize(data)
freq = count_freq(tokens)
top = top_n(freq, 5)
print(top)

data = input()
data = normalize(data)
tokens = tokenize(data)
freq = count_freq(tokens)
top = top_n(freq, 5)


print(f'Всего слов: {len(tokens)}')
print(f'Уникальных слов: {len(freq)}')
print("Топ-5:")
for el in top:
    print(f'{el[0]}:{el[1]}')

print_table(top)'''