from _distance import show as show_distance
from _circle import show as show_circle
from _operations import show as show_operations
from _favorite_movies import show as show_fav_movies
from _my_family import show as show_family
from _zoo import show as show_secret_zoo
from _songs_list import show as show_songs
from _secret import show as show_secret
from _garden import show as show_garden
from _shopping import show as show_shopping
from _store import show as show_store


def main():
    tasks = [
        show_distance,
        show_circle,
        show_operations,
        show_fav_movies,
        show_family,
        show_secret_zoo,
        show_songs,
        show_secret,
        show_garden,
        show_shopping,
        show_store
    ]


    while True:
        print("Выберите задание:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. Задание {i}")

        choice = input("Введите номер задания: ")
        if choice == '-1':
            return

        if choice.isdigit() and 1 <= int(choice) <= len(tasks):
            tasks[int(choice) - 1]()
        else:
            print("Неверный номер задания. Пожалуйста, попробуйте снова.")


if __name__ == "__main__":
    main()
