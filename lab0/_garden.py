#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def get_flower_sets(garden, meadow):
    """Создание множеств цветов из сада и луга."""
    garden_set = set(garden)
    meadow_set = set(meadow)
    return garden_set, meadow_set

def print_flower_info(garden_set, meadow_set):
    """Вывод информации о цветах."""
    print("Все виды цветов в саду:", garden_set)
    print("Все виды цветов на лугу:", meadow_set)

    print("Цветы, которые растут и там, и там:", garden_set & meadow_set)
    print("Цветы, которые растут в саду, но не растут на лугу:", garden_set - meadow_set)
    print("Цветы, которые растут на лугу, но не растут в саду:", meadow_set - garden_set)

def get_flower_input(prompt):
    """Получение списка цветов от пользователя с триммингом."""
    flowers = input(prompt)
    return tuple(flower.strip() for flower in flowers.split(','))

def main():
    """Основная функция для отображения информации о цветах."""
    garden = get_flower_input("Введите цветы, сорванные в саду (через запятую): ")
    meadow = get_flower_input("Введите цветы, сорванные на лугу (через запятую): ")

    garden_set, meadow_set = get_flower_sets(garden, meadow)
    print_flower_info(garden_set, meadow_set)

if __name__ == "__main__":
    main()
