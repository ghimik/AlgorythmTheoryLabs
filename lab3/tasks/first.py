import random

notes = ['до', 'ре', 'ми', 'фа', 'соль', 'ля', 'си']

def random_note_generator():
    for _ in range(1_000_000):
        yield random.choice(notes)


def generate_random_notes():
    generator = random_note_generator()
    return [next(generator) for _ in range(20)]

print(generate_random_notes())
