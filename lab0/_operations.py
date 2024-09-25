import itertools


# генерация всех операций
def generate_operations(operations, length):
    return list(itertools.product(operations, repeat=length))


# генерация всех скобок
def generate_expressions(numbers, operations):
    if len(numbers) == 1:
        return [str(numbers[0])]

    expressions = []
    for i in range(len(numbers) - 1):
        left_numbers = numbers[:i + 1]
        right_numbers = numbers[i + 1:]

        left_expressions = generate_expressions(left_numbers, operations)
        right_expressions = generate_expressions(right_numbers, operations)

        for left in left_expressions:
            for right in right_expressions:
                for operation in operations:
                    expressions.append(f'({left} {operation} {right})')

    return expressions


def generate_all_expressions(numbers):
    operations = ['+', '-', '*', '/']
    expressions = []

    # все комбинации операций
    for ops in generate_operations(operations, len(numbers) - 1):
        # все выражения с текущими операциями
        exprs = generate_expressions(numbers, ops)
        expressions.extend(exprs)

    return expressions


def filter_expressions(expressions, target):
    valid_expressions = []
    for expr in expressions:
        try:
            if eval(expr) == target:
                valid_expressions.append(expr)
        except ZeroDivisionError:
            continue
    return valid_expressions


if __name__ == "__main__":
    input_numbers = input("Введите набор чисел, разделенных пробелами (например, 1 2 3 4 5): ")
    numbers = list(map(int, input_numbers.split()))

    target_value = int(input("Введите целевое значение: "))

    all_expressions = generate_all_expressions(numbers)
    valid_expressions = filter_expressions(all_expressions, target_value)

    # Вывод всех подходящих выражений
    if valid_expressions:
        print(f"Найденные выражения, равные {target_value}:")
        for expression in valid_expressions:
            print(expression)
    else:
        print(f"Выражения, равные {target_value}, не найдены.")
