#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math


def calculate_circle_area(radius):
    """Вычисление площади круга с заданным радиусом."""
    return round(math.pi * radius ** 2, 4)


def calculate_distance_from_origin(point):
    """Вычисление расстояния от точки до начала координат (0, 0)."""
    return math.sqrt(point[0] ** 2 + point[1] ** 2)


def is_point_inside_circle(point, radius):
    """Проверка, находится ли точка внутри круга с центром в (0, 0)."""
    return calculate_distance_from_origin(point) <= radius


def get_circle_radius():
    """Получение радиуса круга от пользователя."""
    return float(input("Введите радиус круга: "))


def get_point_coordinates():
    """Получение координат точки от пользователя."""
    x = float(input("Введите координату X точки: "))
    y = float(input("Введите координату Y точки: "))
    return (x, y)


def show_circle_area(radius):
    """Вывод площади круга."""
    area = calculate_circle_area(radius)
    print(f"Площадь круга с радиусом {radius}: {area}")


def show_point_position(point, radius):
    """Проверка и вывод, находится ли точка внутри круга."""
    inside = is_point_inside_circle(point, radius)
    print(f"Точка с координатами {point} внутри круга: {inside}")


def main():
    """Основная функция программы."""
    radius = get_circle_radius()

    point_1 = get_point_coordinates()
    point_2 = get_point_coordinates()

    show_circle_area(radius)

    show_point_position(point_1, radius)
    show_point_position(point_2, radius)


if __name__ == "__main__":
    main()
