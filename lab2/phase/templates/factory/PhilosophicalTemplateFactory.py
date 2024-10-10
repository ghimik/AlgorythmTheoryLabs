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


def romantic_template_four(word_set):
    noun = word_set.get_random_noun()
    adjective = word_set.get_random_adjective()
    return f"Ты — моя {adjective} {noun}, которая наполняет жизнь смыслом."


def romantic_template_five(word_set):
    verb1 = word_set.get_random_verb()
    verb2 = word_set.get_random_verb()
    return f"С тобой я хочу {verb1} и {verb2} вечность."


def romantic_template_six(word_set):
    noun = word_set.get_random_noun()
    return f"Каждый момент с тобой — это {noun}, которое я храню в сердце."


def romantic_template_seven(word_set):
    adjective = word_set.get_random_adjective()
    return f"Ты — моя {adjective} звезда на небосклоне жизни."


def romantic_template_eight(word_set):
    noun1 = word_set.get_random_noun()
    noun2 = word_set.get_random_noun()
    return f"{noun1} и {noun2} — это два сердца, бьющихся в унисон."


class RomanticTemplateFactory(TemplateFactory):
    def __init__(self):
        self.templates = [
            romantic_template_one,
            romantic_template_two,
            romantic_template_three,
            romantic_template_four,
            romantic_template_five,
            romantic_template_six,
            romantic_template_seven,
            romantic_template_eight
        ]

    def create_template(self):
        return random.choice(self.templates)
