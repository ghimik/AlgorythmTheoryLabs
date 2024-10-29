import random
import concurrent.futures

notes = ['до', 'ре', 'ми', 'фа', 'соль', 'ля', 'си']

def random_note_generator():
    for _ in range(1_000_000):
        yield random.choice(notes)


def generate_random_notes():
    generator = random_note_generator()
    return [next(generator) for _ in range(20)]

def random_note_worker(num_notes):
    return [random.choice(notes) for _ in range(num_notes)]

def generate_random_notes_multi_thread(num_threads=4):
    notes_per_thread = 1_000_000 // num_threads
    with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
        results = list(executor.map(random_note_worker, [notes_per_thread] * num_threads))
    return [note for sublist in results for note in sublist]

