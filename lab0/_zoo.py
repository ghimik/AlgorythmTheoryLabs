#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def display_zoo(zoo):
    """Выводит список животных в зоопарке."""
    print("Список животных в зоопарке:", zoo)


def display_birds(birds):
    """Выводит список птиц."""
    print("Список птиц:", birds)


def add_animal(zoo):
    """Добавляет животное в зоопарк по выбору пользователя."""
    animal = input("Введите имя животного, которое хотите добавить: ").strip()
    position = input("Введите позицию (1 - в начало, 2 - в конец, 3 - между существующими животными): ").strip()

    if position == '1':
        zoo.insert(0, animal)
    elif position == '2':
        zoo.append(animal)
    elif position == '3':
        index = int(input("Введите индекс, между какими животными добавить (1 для 1-го, 2 для 2-го и т.д.): ")) - 1
        if 0 <= index < len(zoo):
            zoo.insert(index + 1, animal)
        else:
            print("Недопустимый индекс.")
    else:
        print("Недопустимая позиция.")


def remove_animal(zoo):
    """Удаляет животное из зоопарка по выбору пользователя."""
    animal = input("Введите имя животного, которое хотите убрать: ").strip()
    if animal in zoo:
        zoo.remove(animal)
    else:
        print("Животное не найдено в зоопарке.")


def add_bird(birds):
    """Добавляет птицу в список птиц по выбору пользователя."""
    bird = input("Введите имя птицы, которую хотите добавить: ").strip()
    birds.append(bird)


def remove_bird(birds):
    """Удаляет птицу из списка птиц по выбору пользователя."""
    bird = input("Введите имя птицы, которую хотите убрать: ").strip()
    if bird in birds:
        birds.remove(bird)
    else:
        print("Птица не найдена в списке.")


def show_animal_positions(zoo):
    """Показывает позиции льва и жаворонка в зоопарке."""
    if 'lion' in zoo:
        print(f"Лев находится в клетке: {zoo.index('lion') + 1}")
    if 'lark' in zoo:
        print(f"Жаворонок находится в клетке: {zoo.index('lark') + 1}")


def main():
    zoo = ['lion', 'kangaroo', 'elephant', 'monkey']
    birds = []

    while True:
        action = input(
            "Введите действие (добавить животное/убрать животное/показать животных/добавить птицу/убрать птицу/показать птиц/выход): ").strip().lower()

        if action == 'добавить животное':
            add_animal(zoo)
        elif action == 'убрать животное':
            remove_animal(zoo)
        elif action == 'показать животных':
            display_zoo(zoo)
        elif action == 'добавить птицу':
            add_bird(birds)
        elif action == 'убрать птицу':
            remove_bird(birds)
        elif action == 'показать птиц':
            display_birds(birds)
        elif action == 'выход':
            break
        else:
            print("Недопустимая команда.")

    show_animal_positions(zoo)


if __name__ == "__main__":
    main()
