import random

from lab2.phase.templates.factory.TemplateFactory import TemplateFactory

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

def philosophical_template_four(word_set):
    noun1 = word_set.get_random_noun()
    noun2 = word_set.get_random_noun()
    return f"{noun1} и {noun2} — две стороны одной медали."


def philosophical_template_five(word_set):
    verb = word_set.get_random_verb()
    return f"Истина заключается в том, что мы должны {verb}."


def philosophical_template_six(word_set):
    adjective = word_set.get_random_adjective()
    return f"Жизнь — это {adjective} путь, полный открытий."


def philosophical_template_seven(word_set):
    noun = word_set.get_random_noun()
    return f"{noun} — это зеркало нашей души."


def philosophical_template_eight(word_set):
    verb1 = word_set.get_random_verb()
    verb2 = word_set.get_random_verb()
    return f"Мы можем {verb1} или {verb2}, но важно не терять себя."


class PhilosophicalTemplateFactory(TemplateFactory):
    def __init__(self):
        self.templates = [
            philosophical_template_one,
            philosophical_template_two,
            philosophical_template_three,
            philosophical_template_four,
            philosophical_template_five,
            philosophical_template_six,
            philosophical_template_seven,
            philosophical_template_eight
        ]

    # override
    def create_template(self):
        return random.choice(self.templates)
