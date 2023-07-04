num = 0

if num >= 0:
    print('Число болше либо равно 0')
else:
    print('Число отрицательное')


str_1 = 'test'
str_2 = 'test1'

if str_1 in str_2:
    print('ДА')
else:
    print('НЕТ')


num_float = -5.3
if num_float > 0:
    print('Положительное число')
elif num_float == 0:
    print('Ноль')
else:
    print('Число отрицательное')


permit_print = True

if num > 0 and permit_print:
    print('num - положительное число')
elif not permit_print:
    print('Печать запрещена')



