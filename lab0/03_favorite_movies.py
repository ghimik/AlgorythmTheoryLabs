#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть строка с перечислением фильмов

my_favorite_movies = 'Терминатор, Пятый элемент, Аватар, Чужие, Назад в будущее'

# Выведите на консоль с помощью индексации строки, последовательно:
#   первый фильм
#   последний
#   второй
#   второй с конца

# Запятая не должна выводиться.  Переопределять my_favorite_movies нельзя
# Использовать .split() или .find()или другие методы строки нельзя - пользуйтесь только срезами,
# как указано в задании!

first_movie = my_favorite_movies[:10]
last_movie = my_favorite_movies[42:]
second_movie = my_favorite_movies[12:25]
second_last_movie = my_favorite_movies[35:40]

print(first_movie)
print(last_movie)
print(second_movie)
print(second_last_movie)