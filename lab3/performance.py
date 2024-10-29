import time

from lab3.tasks.first import random_note_generator, generate_random_notes_multi_thread


def generate_random_notes_single_thread():
    return [note for note in random_note_generator()]


def performance_comparison():
    start_single = time.time()
    generate_random_notes_single_thread()
    end_single = time.time()

    start_multi = time.time()
    generate_random_notes_multi_thread(num_threads=8)
    end_multi = time.time()

    print(f"Однопоточная версия: {end_single - start_single:.2f} секунд")
    print(f"Многопоточная версия: {end_multi - start_multi:.2f} секунд")


if __name__ == '__main__':
    performance_comparison()