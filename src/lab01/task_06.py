n = int(input('Количество учеников: '))
tr = 0
fl = 0
for i in range(n):
    sin = input('in_%s: ' %(i+1))
    data = sin.split()
    if data[3] == 'True':
        tr += 1
    else:
        fl += 1
print(tr, fl)