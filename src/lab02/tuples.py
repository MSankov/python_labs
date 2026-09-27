def format_record(rec: tuple[str, str, float]):
    '''
    Возвращает строку вида: Иванов И.И., гр. BIVT-25, GPA 4.60

    Args:
        rec: tuple[str, str, float]
    
    Returns:
        str
    
    Raises:
        ValueError: если аргумент недопустимого значения
        TypeError: если аргумент недопустимого типа
    '''
    if len(rec) != 3:
        raise ValueError('Несоответствует количество элементов')
    if type(rec[0]) != str:
        raise TypeError('первый аргумент недопустимого типа')
    if type(rec[1]) != str:
        raise TypeError('второй аргумент недопустимого типа')
    if type(rec[2]) != float:
        raise TypeError('третий аргумент недопустимого типа')
    if rec[2]>5.0 or rec[2] < 0:
        raise ValueError('0.0 <= GPA <= 5.0')
    el = []
    fio = rec[0].strip()
    fio = fio.split()
    if len(fio) not in (2,3):
        raise ValueError('ФИ(О) заданы неверно')
    
    fio[0] = fio[0][0].upper() + fio[0][1:].lower() # заглавная буква в фамилии
    fio[1] = fio[1][0].upper() + fio[1][1:].lower() # заглавная буква в имени
    fio_res = fio[0] +' '+ fio[1][0]+'.'
    if len(fio) == 3:
        fio[2] = fio[2][0].upper() + fio[2][1:].lower()
        fio_res += fio[2][0] + '.'

    gr = rec[1].strip().upper()
    if len(gr) <= 0:
        raise ValueError('Напишите группу')

    gpa = rec[2]

    res = f'{fio_res}, гр. {gr}, GPA {gpa:.2f}'
    return res
print(format_record(("Иванов Иван Иванович", "BIVT-25", 4.6)))
print(format_record(("Петров Пётр", "IKBO-12", 5.0)))
print(format_record(("Петров Пётр Петрович", "IKBO-12", 5.0)))
print(format_record(("  сидорова  анна   сергеевна ", "ABB-01", 3.999)))