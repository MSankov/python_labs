
snnf = input('ФИО: ')
m = snnf.split()
#n = snnf.split(' ')
#print(m,n)
inc = ''
for i in m:
    inc += (i[0]).upper()
print('Инициалы: %s' %(inc))
print('Длина (символов): %s' %(len(' '.join(m))))

