from typing import List


def compare(x, y):
    if x > y:
        print(x)
    elif y > x:
        print(y)
    else:
        print("Числа равны")


compare(6, 8)
compare(10, 8)
compare(8, 8)


def diff_equal_135(x, y):
    if abs(x - y) == 135:
        print("YES")
    else:
        print("NO")


diff_equal_135(136, 1)
diff_equal_135(5, 6)


def seasons(x):
    if x == 1 or x == 2 or x == 12:
        print('Зима')
    elif 3 <= x <= 5:
        print('Весна')
    elif 6 <= x <= 8:
        print('Лето')
    elif 9 <= x <= 11:
        print("Осень")
    else:
        print("Введите число от 1 до 12")


seasons(1)
seasons(25)


def compare_10(x, y, z):
    if x > 10 and y > 10 and z > 10:
        print("yes")
    else:
        print("no")


compare_10(11, 1, 13)
compare_10(11, 12, 13)


def positive_num_list(li: List[int]):
    if len(li) != 5:
        print("Введите пять элементов")
        return

    count = 0
    for item in li:
        if item > 0:
            count += 1
    print(count)


positive_num_list([1, -3, -3, 8, -7])
positive_num_list([1, -3, -3, 8, -7, 9])


def count_days(years, months):
    print((years * 12 + months) * 29)


count_days(5, 7)
