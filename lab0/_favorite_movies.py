#!/usr/bin/env python3
# -*- coding: utf-8 -*-
DELIMETER = ','

def get_favorite_movies():
    """Возвращает строку с любимыми фильмами."""
    return input("Введите фильмы: ") or 'Терминатор, Пятый элемент, Аватар, Чужие, Назад в будущее'

def extract_movies(movies_string):
    """Извлекает фильмы из строки и возвращает список."""
    comma_positions = [-2]
    for i in range(len(movies_string)):
        if movies_string[i] == DELIMETER:
            comma_positions.append(i)
    comma_positions.append(len(movies_string))

    movies = [
        movies_string[:comma_positions[1]],
        movies_string[comma_positions[-2] + 2:],
        movies_string[comma_positions[1] + 2:comma_positions[2]],
        movies_string[comma_positions[-3] + 2:comma_positions[-2]],
    ]
    return movies

def show_movies():
    """Выводит на консоль любимые фильмы."""
    movies_string = get_favorite_movies()
    movies = extract_movies(movies_string)

    # Выводим результаты
    for movie in movies:
        print(movie)

if __name__ == "__main__":
    show_movies()
