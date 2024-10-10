from abc import ABC, abstractmethod

from lab2.phase.WordSet import WordSet


class WordsProvider(ABC):
    @abstractmethod
    def get_nouns(self):
        pass

    @abstractmethod
    def get_verbs(self):
        pass

    @abstractmethod
    def get_adjectives(self):
        pass

    def generate_word_set(self) -> WordSet:
        return WordSet(self.get_nouns(), self.get_verbs(), self.get_adjectives())