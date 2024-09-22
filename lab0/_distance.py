#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math

def show():

    def calculate_distance(coord1, coord2):
        return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

    # Функция для заполнения словаря расстояний
    def fill_distances(sites):
        distances = {}
        for city1, coord1 in sites.items():
            distances[city1] = {}
            for city2, coord2 in sites.items():
                if city1 != city2:
                    distances[city1][city2] = round(calculate_distance(coord1, coord2), 2)
        return distances

    # Есть словарь координат городов

    sites = {
        'Moscow': (550, 370),
        'London': (510, 510),
        'Paris': (480, 480),
    }

    # Составим словарь словарей расстояний между ними
    # расстояние на координатной сетке - ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

    distances = fill_distances(sites)


    print(distances)




