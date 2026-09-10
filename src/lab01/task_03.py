price = float(input('Цена: '))
discount = float(input('Скиндка: '))
vat = float(input('НДС: '))

base = price * (1 - discount/100)
vat_amount = base * (vat/100)
total = base + vat_amount

base = f'base = {base:.2f}'
vat_amount = f'vat_amount = {vat_amount:.2f}'
total = f'total = {total:.2f}'

print('База после скидки: %s ₽' % base)
print('НДС: %s ₽' % vat_amount)
print('Итого к оплате: %s ₽' % total)