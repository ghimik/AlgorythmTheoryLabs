import random


class WordSet:
    def __init__(self, nouns, verbs, adjectives):
        self.nouns = nouns
        self.verbs = verbs
        self.adjectives = adjectives

    def get_random_noun(self):
        print(self.nouns)
        return random.choice(self.nouns)

    def get_random_verb(self):
        print(self.verbs)
        return random.choice(self.verbs)

    def get_random_adjective(self):
        print(self.adjectives)
        return random.choice(self.adjectives)

    def __str__(self):
        return (f'nouns: {self.nouns},'
                f'verbs: {self.verbs}, '
                f'adjectives: {self.adjectives}')