import random

from lab2.phase.templates.factory.TemplateFactory import TemplateFactory


def romantic_template_one(word_set):
    noun = word_set.get_random_noun()
    verb = word_set.get_random_verb()
    return f"Любовь одна, а {noun} много. Только {verb} горит в сердце."


def romantic_template_two(word_set):
    noun1 = word_set.get_random_noun()
    noun2 = word_set.get_random_noun()
    return f"{noun1} — это не просто {noun2}, это мечта!"


def romantic_template_three(word_set):
    verb = word_set.get_random_verb()
    return f"В жизни важно не только {verb}, но и чувствовать!"


class RomanticTemplateFactory(TemplateFactory):
    def __init__(self):
        self.templates = [romantic_template_one, romantic_template_two, romantic_template_three]

    def create_template(self):
        return random.choice(self.templates)
