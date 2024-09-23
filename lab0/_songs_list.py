#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def get_songs_input():
    songs = []
    while True:
        song_name = input("Введите название песни (или 'stop' для завершения): ")
        if song_name.lower() == 'stop':
            break
        duration = input("Введите продолжительность песни в минутах: ")
        songs.append([song_name, float(duration)])
    return songs

def calculate_total_time(songs, song_titles):
    return sum(round(song[1], 2) for song in songs if song[0] in song_titles)

def show():
    violator_songs_list = [
        ['World in My Eyes', 4.86],
        ['Sweetest Perfection', 4.43],
        ['Personal Jesus', 4.56],
        ['Halo', 4.9],
        ['Waiting for the Night', 6.07],
        ['Enjoy the Silence', 4.20],
        ['Policy of Truth', 4.76],
        ['Blue Dress', 4.29],
        ['Clean', 5.83],
    ]

    print("Вы можете ввести свои песни и их продолжительность. Для завершения введите 'stop'.")
    user_songs = get_songs_input()

    if not user_songs:
        user_songs = violator_songs_list

    songs_to_sum_list = ['Halo', 'Enjoy the Silence', 'Clean']
    total_time_list = calculate_total_time(user_songs, songs_to_sum_list)
    print(f'Три песни звучат {total_time_list:.2f} минут')

    violator_songs_dict = {
        'World in My Eyes': 4.76,
        'Sweetest Perfection': 4.43,
        'Personal Jesus': 4.56,
        'Halo': 4.30,
        'Waiting for the Night': 6.07,
        'Enjoy the Silence': 4.6,
        'Policy of Truth': 4.88,
        'Blue Dress': 4.18,
        'Clean': 5.68,
    }

    songs_to_sum_dict = ['Sweetest Perfection', 'Policy of Truth', 'Blue Dress']
    total_time_dict = sum(
        round(violator_songs_dict[song], 2) for song in songs_to_sum_dict
    )
    print(f'А другие три песни звучат {total_time_dict:.2f} минут')

if __name__ == "__main__":
    show()
