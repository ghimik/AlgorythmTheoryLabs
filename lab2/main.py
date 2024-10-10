from lab2.data.InMemoryWordsProvider import InMemoryWordsProvider
from lab2.data.WordsProvider import WordsProvider
from lab2.phase.templates.factory.GangstaTemplateFactory import GangstaTemplateFactory
from lab2.phase.templates.factory.PhilosophicalTemplateFactory import RomanticTemplateFactory
from lab2.phase.templates.factory.RomanticTemplateFactory import PhilosophicalTemplateFactory

words_provider: WordsProvider = InMemoryWordsProvider()

word_set = words_provider.generate_word_set()

gangsta_factory = GangstaTemplateFactory()
romantic_factory = RomanticTemplateFactory()
philosophical_factory = PhilosophicalTemplateFactory()

def generate_phrases():
    print("=== Gangsta Quotes ===")
    for _ in range(3):
        gangsta_template = gangsta_factory.create_template()
        print(gangsta_template(word_set))

    print("\n=== Romantic Quotes ===")
    for _ in range(3):
        romantic_template = romantic_factory.create_template()
        print(romantic_template(word_set))

    print("\n=== Philosophical Quotes ===")
    for _ in range(3):
        philosophical_template = philosophical_factory.create_template()
        print(philosophical_template(word_set))

generate_phrases()
