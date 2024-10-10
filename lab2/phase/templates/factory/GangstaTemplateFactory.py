from lab2.phase.Adjective import Adjective
from lab2.phase.Noun import Noun
from lab2.phase.Verb import Verb
from lab2.phase.WordSet import WordSet
from lab2.phase.templates.GangstaTemplate import GangstaTemplate
from lab2.phase.templates.factory.TemplateFactory import TemplateFactory

class GangstaTemplateFactory(TemplateFactory):
    def create_template(self):
        gangsta_words = WordSet(

            # TODO ПОЛУЧЕНИЕ ИЗВНЕ

            nouns=[Noun("волк"), Noun("пацан"), Noun("орел")],
            verbs=[Verb("бежит"), Verb("дерется"), Verb("падает")],
            adjectives=[Adjective("хитрый"), Adjective("сильный"), Adjective("мудрый")]
        )
        return GangstaTemplate(gangsta_words)