import re

def normalize(text: str, *, casefold: bool = True, yo2e: bool = True):
    '''Убирает невидимые управляющие символы (например, \t, \r) → заменяет на пробелы,
        схлопывает повторяющиеся пробелы в один.
    
        Args:
            text: str, 
            casefold: bool = True, (Если casefold=True — привести к casefold. Если casefold=False - используем lower().)
            yo2e: bool = True (Если yo2e=True — заменить все ё/Ё на е/Е.)
        
        Returns:
            str
    
        Raises:
        '''
    
    if casefold:
        text = text.casefold()
    else:
        text = text.lower()

    if yo2e:
        text = text.replace('ё', 'е')

    text = " ".join(text.split())
    return text

def tokenize(text: str):
    '''Разбить на «слова» по небуквенно-цифровым разделителям.
    
        Args:
            text: str
        
        Returns:
            list[str]
    '''
    res = re.findall(r"\w+(?:-\w+)*",text)
    return res

def count_freq(tokens: list[str]):
    '''Подсчитать частоты, вернуть словарь слово → количество.
    
        Args:
            list[str]
        
        Returns:
            dict[str, int]
    '''
    res = {}
    for s in tokens:
        if s in res:
            res[s]+=1
        else:
            res[s] = 1
    return res

def top_n(freq: dict[str, int], n: int = 5):
    '''Вернуть топ-N по убыванию частоты; при равенстве — по алфавиту слова.
    
    Args:
        list[str]
        
    Returns:
        list[tuple[str, int]]
    '''
    res = []
    items = list(freq.items())
    #dict_items([('a', 3), ('b', 2), ('c', 1)])
    for i in range(len(items)-1):
        for j in range(i+1, len(items)):
            if items[j][1] > items[i][1]:
                (items[i], items[j]) = (items[j], items[i])
            elif items[j][1] == items[i][1] and items[j][0] < items[i][0]:
                (items[i], items[j]) = (items[j], items[i])

    return items[:n]

def print_table(data: dict[str, int]):
    max_len = 5
    for el in data:
        if len(el[0]) > max_len:
            max_len = len(el[0])

    print(f'{'слово':{max_len}} | частота')
    print('-'*(max_len+12))
    for el in data:
        print(f'{el[0]:{max_len}} | {el[1]:^7}')