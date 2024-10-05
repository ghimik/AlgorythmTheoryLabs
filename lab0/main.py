from _distance import main as show_distance
from _circle import main as show_circle
from _operations import main as show_operations
from _favorite_movies import show_movies as show_fav_movies
from _my_family import main as show_family
from _zoo import main as show_secret_zoo
from _songs_list import main as show_songs
from _secret import main as show_secret
from _garden import main as show_garden
from _shopping import main as show_shopping
from _store import main as show_store


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
