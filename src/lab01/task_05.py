snnf = input('ФИО: ')
m = snnf.split()
inc = ''
for i in m:
    inc += i[0]
print('Инициалы: %s' %(inc))
print('Длина (символов): %s' %(len(snnf)))

