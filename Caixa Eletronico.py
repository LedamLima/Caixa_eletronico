from random import randint
from math import radians
from math import remainder
print('####'*10)
print('==='*10)
print('{:^30}'.format('Banco Inovação'))
print('==='*10)
valor = int(input('Que valor vc quer sacar? R$  '))
total = valor
céd = 50
totcéd = 0
while True:
    if total >= céd:
        total -= céd
        totcéd += 1
    else:
        print(f'Total de {totcéd} células de R$ {céd} ')
        if céd == 50:
            céd = 20
        elif céd == 20:
            céd = 10
        elif céd == 10:
            céd = 1
        if total == 0:
            break
         
print ('####'*10)

    

