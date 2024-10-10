import random


class WordSet:
    def __init__(self, nouns, verbs, adjectives):
        self.nouns = nouns
        self.verbs = verbs
        self.adjectives = adjectives

    def get_random_noun(self):
        return random.choice(self.nouns)

    def get_random_verb(self):
        return random.choice(self.verbs)

    def get_random_adjective(self):
        return random.choice(self.adjectives)