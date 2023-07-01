a: int = 5
b: str = 'строка'
c: list = [1, 2]


def indent(s: str, width: int) -> str:
    return " " * (max(0, width - len(s))) + s


print(indent('123', 123))


def len_str(d: str = '') -> int:
    return len(d)


print(len_str())


def len_lists(l1: list, l2: list) -> int:
    return max(len(l1), len(l2))


print(len_lists([1, 2, 3, 4], [5, 6, 7, 8, 9]))


def add(l, x):
    l.append(x)
    return l


print(add(['1', '2', '3'], '4'))


def sum(list2):
    s = 0
    for i in list2:
        s += i
    return s


print(sum([1, 2, 3, 4]))

