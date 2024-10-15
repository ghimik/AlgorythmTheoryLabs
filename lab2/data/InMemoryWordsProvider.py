from data.WordsProvider import WordsProvider
from words.Adjective import Adjective
from words.Noun import Noun
from words.Verb import Verb


class InMemoryWordsProvider(WordsProvider):
    def __init__(self):
        self.nouns = [
            Noun("свет"), Noun("тень"), Noun("жизнь"), Noun("сердце"), Noun("любовь"),
            Noun("душа"), Noun("путь"), Noun("мир"), Noun("мысль"), Noun("мечта"),
            Noun("светило"), Noun("песня"), Noun("время"), Noun("реальность"), Noun("чувство")
        ]
        self.verbs = [
            Verb("гореть"), Verb("блестеть"), Verb("лететь"), Verb("кружиться"), Verb("цвести"),
            Verb("жить"), Verb("мечтать"), Verb("забывать"), Verb("искать"), Verb("понимать"),
            Verb("светить"), Verb("танцевать"), Verb("слушать"), Verb("крикнуть"), Verb("петь")
        ]
        self.adjectives = [
            Adjective("яркий"), Adjective("грустный"), Adjective("волнительный"), Adjective("светлый"),
            Adjective("красивый"), Adjective("нежный"), Adjective("беспечный"), Adjective("сильный"),
            Adjective("удивительный"), Adjective("мудрый"), Adjective("неизведанный"), Adjective("магический"),
            Adjective("потрясающий"), Adjective("глубокий"), Adjective("умиротворяющий"), Adjective("тёплый")
        ]

    def get_nouns(self):
        return self.nouns

    def get_verbs(self):
        return self.verbs

    def get_adjectives(self):
        return self.adjectives

    def add_noun(self, noun):
        self.nouns.append(noun)

    def add_verb(self, verb):
        self.verbs.append(verb)

    def add_adjective(self, adj):
        self.adjectives.append(adj)
