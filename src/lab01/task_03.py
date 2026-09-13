price = float(input('Цена: '))
discount = float(input('Скиндка: '))
vat = float(input('НДС: '))

base = price * (1 - discount/100)
vat_amount = base * (vat/100)
total = base + vat_amount

#base = f'base = {base:.2f}'
#vat_amount = f'vat_amount = {vat_amount:.2f}'
#total = f'total = {total:.2f}'

print(f'{"База после скидки:":>20} {base:.2f} ₽')
print(f'{"НДС:":>20} {vat_amount:.2f}  ₽')
print(f'{"Итого к оплате:":>20} {total:.2f} ₽')