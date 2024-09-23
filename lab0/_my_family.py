#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def get_family_data():
    """Получение данных о семье от пользователя."""
    my_family = []
    my_family_height = []

    num_members = int(input("Введите количество членов семьи: "))

    for _ in range(num_members):
        name = input("Введите имя члена семьи: ")
        height = int(input(f"Введите рост {name} в см: "))
        my_family.append(name)
        my_family_height.append([name, height])

    return my_family, my_family_height


def print_family_info(my_family_height):
    """Вывод информации о семье."""
    father_height = my_family_height[1][1] if len(my_family_height) > 1 else 'не указан'
    print(f'Рост отца - {father_height} см')

    total_height = sum(member[1] for member in my_family_height)
    print(f'Общий рост моей семьи - {total_height} см')


def main():
    """Основная функция для отображения информации о семье."""
    my_family, my_family_height = get_family_data()
    print_family_info(my_family_height)


if __name__ == "__main__":
    main()
