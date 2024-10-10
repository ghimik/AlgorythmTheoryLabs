from lab2.phase.Adjective import Adjective
from lab2.phase.Noun import Noun
from lab2.phase.Verb import Verb
from lab2.phase.WordSet import WordSet
from lab2.phase.templates.RomanticTemplate import RomanticTemplate
from lab2.phase.templates.factory.TemplateFactory import TemplateFactory

class RomanticTemplateFactory(TemplateFactory):
    def create_template(self):
        romantic_words = WordSet(

            # TODO ПОЛУЧЕНИЕ ИЗВНЕ

            nouns=[Noun("соблазнов"), Noun("счетов"), Noun("заботы")],
            verbs=[Verb("горит"), Verb("светит"), Verb("скрывается")],
            adjectives=[Adjective("вечная"), Adjective("забытая"), Adjective("яркая")]
        )
        return RomanticTemplate(romantic_words)