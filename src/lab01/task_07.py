#Первая заглавная буква в строке является первой буквой в оригинальной строке;
#Символы оригинальной строки расположены в фиксированном шаге друг от друга;
#Второй символ стоит сразу после цифры;
#Последним символом оригинальной строки является точка .
#in: thisisabracadabraHt1eadljjl12ojh.
#out: Hello.
code = input('in: ')
s = ''
IDletter1 = 0
IDletter2 = 0
for i in range(len(code)):
    if code[i] != (code[i]).lower():
        IDletter1 = i
        break
for i in range(len(code)):
    if code[i] in '0123456789':
        IDletter2 = i
        break
step = abs(IDletter2-IDletter1)
lastletter = IDletter1
st = 2
for i in range(IDletter1,len(code)):
    if code[i] == '.':
        break
    if st == step:
        st = 0
        s += code[i]
    else:
        st+=1
print(s)
