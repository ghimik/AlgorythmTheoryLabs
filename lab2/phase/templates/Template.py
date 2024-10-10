from abc import ABC, abstractmethod


class Template(ABC):
    def __init__(self, word_set):
        self.word_set = word_set

    @abstractmethod
    def generate_phrase(self):
        pass