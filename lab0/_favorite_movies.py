#!/usr/bin/env python3
# -*- coding: utf-8 -*-
DELIMETER = ','
# Есть строка с перечислением фильмов
def show():
    my_favorite_movies = 'Терминатор, Пятый элемент, Аватар, Чужие, Назад в будущее'

    # Выведите на консоль с помощью индексации строки, последовательно:
    #   первый фильм
    #   последний
    #   второй
    #   второй с конца

    # Запятая не должна выводиться.  Переопределять my_favorite_movies нельзя
    # Использовать .split() или .find()или другие методы строки нельзя - пользуйтесь только срезами,
    # как указано в задании!

    comma_positions = [-2]
    for i in range(len(my_favorite_movies)):
        if my_favorite_movies[i] == DELIMETER:
            comma_positions.append(i)
    comma_positions.append(len(my_favorite_movies))

    first_movie = my_favorite_movies[:comma_positions[1]]
    last_movie = my_favorite_movies[comma_positions[-2] + 2:]
    second_movie = my_favorite_movies[comma_positions[1] + 2:comma_positions[2]]
    second_last_movie = my_favorite_movies[comma_positions[-3] + 2:comma_positions[-2]]

    # Выводим результаты
    print(first_movie)
    print(last_movie)
    print(second_movie)
    print(second_last_movie)

show()