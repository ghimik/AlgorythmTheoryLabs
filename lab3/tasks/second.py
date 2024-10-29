def multiples_of_three(a):
    if not isinstance(a, int):
        raise ValueError("Аргумент должен быть целым числом.")

    if a % 3 != 0:
        a += (3 - a % 3)

    while True:
        yield a
        a += 3

