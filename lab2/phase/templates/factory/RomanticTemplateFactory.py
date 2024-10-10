import random

from lab2.phase.templates.factory.TemplateFactory import TemplateFactory

class PhilosophicalTemplateFactory(TemplateFactory):
    def __init__(self):
        self.templates = [philosophical_template_one, philosophical_template_two,
                          philosophical_template_three]

    # override
    def create_template(self):
        return random.choice(self.templates)

def philosophical_template_one(word_set):
    verb1 = word_set.get_random_verb()
    verb2 = word_set.get_random_verb()
    noun = word_set.get_random_noun()
    return f"Лучше {verb1} и {verb2}, чем {noun} и потеря."


def philosophical_template_two(word_set):
    noun = word_set.get_random_noun()
    return f"{noun} — это всего лишь вопрос времени."


def philosophical_template_three(word_set):
    verb = word_set.get_random_verb()
    verb1 = word_set.get_random_verb()
    return f"Смысл жизни — это {verb}, а не {verb1}"