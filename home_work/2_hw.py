def task_1() -> None:
    a: int = 5
    print(a, "относится к типу ", type(a))
    b: float = 0.5
    print(b, "относится к типу ", type(b))
    c: str = 'hello'
    print(c, "относится к типу ", type(c))
    d: list = [1, 2]
    print(d, "относится к типу ", type(d))
    e: bool = True
    print(e, "относится к типу ", type(e))


task_1()


# Числа Фибоначчи
def task_2() -> None:
    a = [1, 2, 3, 5, 8, 13, 21]
    print(a[0:3])


task_2()


def task_3(x: float) -> float:
    return x ** 2


print(task_3(5))
print(task_3(1.2))
