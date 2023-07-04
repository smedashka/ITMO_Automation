num = 15
permit_print = True

if num > 0 and permit_print:
    print('num - положительное число')
elif not permit_print:
    print('Печать запрещена')


def student_rank(x):
    if 1 <= x <= 4:
        print('Бакалавр')
    elif 5 <= x <= 6:
        print('Магистр')
    elif 7 <= x <= 9:
        print('Аспирант')
    else:
        print("Введите корректный курс")


student_rank(5)


def name(number):
    if number > 100 or number < -100:
        print('-')
    else:
        print('+')


name(10)
