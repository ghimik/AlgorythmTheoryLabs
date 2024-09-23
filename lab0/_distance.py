#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math

def calculate_distance(coord1, coord2):
    """Вычисление расстояния между двумя координатами."""
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

def fill_distances(sites):
    """Заполнение словаря расстояний между городами."""
    distances = {}
    for city1, coord1 in sites.items():
        distances[city1] = {}
        for city2, coord2 in sites.items():
            if city1 != city2:
                distances[city1][city2] = round(calculate_distance(coord1, coord2), 2)
    return distances

def get_sites_from_input():
    """Получение списка городов и координат от пользователя."""
    sites = {}
    num_sites = int(input("Введите количество городов: "))
    for _ in range(num_sites):
        city = input("Введите название города: ")
        x = int(input(f"Введите координату X для {city}: "))
        y = int(input(f"Введите координату Y для {city}: "))
        sites[city] = (x, y)
    return sites

def show_distances(distances):
    """Вывод словаря расстояний."""
    print("Расстояния между городами:")
    for city, dests in distances.items():
        for dest, distance in dests.items():
            print(f"{city} -> {dest}: {distance} км")

def main():
    sites = get_sites_from_input()

    distances = fill_distances(sites)

    show_distances(distances)

if __name__ == "__main__":
    main()
