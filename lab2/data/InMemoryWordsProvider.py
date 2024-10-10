from lab2.data.WordsProvider import WordsProvider
from lab2.phase.Adjective import Adjective
from lab2.phase.Noun import Noun
from lab2.phase.Verb import Verb


class InMemoryWordsProvider(WordsProvider):
    def __init__(self):
        self.nouns = [Noun("свет"), Noun("тень"), Noun("жизнь"), Noun("сердце"), Noun("любовь")]
        self.verbs = [Verb("гореть"), Verb("блестеть"), Verb("лететь"), Verb("кружиться"), Verb("цвести")]
        self.adjectives = [Adjective("яркий"), Adjective("грустный"), Adjective("волнительный"), Adjective("светлый")]

    def get_nouns(self):
        return self.nouns

    def get_verbs(self):
        return self.verbs

    def get_adjectives(self):
        return self.adjectives