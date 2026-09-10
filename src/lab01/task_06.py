n = int(input('Количество учеников: '))
tr = 0
fl = 0
for i in range(n):
    k = input('in_%s: ' %(i+1))
    if 'True' in k:
        tr += 1
    elif 'False' in k:
        fl += 1
print(tr, fl)