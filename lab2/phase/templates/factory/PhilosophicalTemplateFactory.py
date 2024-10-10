from lab2.phase.Adjective import Adjective
from lab2.phase.Noun import Noun
from lab2.phase.Verb import Verb
from lab2.phase.WordSet import WordSet
from lab2.phase.templates.PhilosoficalTemplate import PhilosophicalTemplate
from lab2.phase.templates.factory.TemplateFactory import TemplateFactory


class PhilosophicalTemplateFactory(TemplateFactory):
    def create_template(self):
        philosophical_words = WordSet(

            # TODO ПОЛУЧЕНИЕ ИЗВНЕ


            nouns=[Noun("жизнь"), Noun("смерть"), Noun("время")],
            verbs=[Verb("опоздать"), Verb("успеть"), Verb("забить")],
            adjectives=[Adjective("важная"), Adjective("глубокая"), Adjective("простая")]
        )
        return PhilosophicalTemplate(philosophical_words)