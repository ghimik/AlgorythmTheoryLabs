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

def romantic_template_nine(word_set):
    noun = word_set.get_random_noun()
    adjective = word_set.get_random_adjective()
    return f"Твоя {adjective} улыбка — как {noun}, который освещает мою жизнь."


def romantic_template_ten(word_set):
    verb = word_set.get_random_verb()
    noun = word_set.get_random_noun()
    return f"Я не могу перестать {verb} о тебе, ты — мое {noun}."


def romantic_template_eleven(word_set):
    noun1 = word_set.get_random_noun()
    noun2 = word_set.get_random_noun()
    return f"Каждый {noun1}, проведенный с тобой, — это {noun2}, полный счастья."


def romantic_template_twelve(word_set):
    adjective = word_set.get_random_adjective()
    noun = word_set.get_random_noun()
    return f"Ты — {adjective} {noun}, которая делает этот мир прекрасным."


def romantic_template_thirteen(word_set):
    verb1 = word_set.get_random_verb()
    verb2 = word_set.get_random_verb()
    noun = word_set.get_random_noun()
    return f"С тобой я готов {verb1} и {verb2}, лишь бы быть рядом и чувствовать {noun}."


def romantic_template_fourteen(word_set):
    adjective1 = word_set.get_random_adjective()
    adjective2 = word_set.get_random_adjective()
    noun = word_set.get_random_noun()
    return f"Ты {adjective1} и {adjective2}, как {noun}, что приносит свет в мою жизнь."


def romantic_template_fifteen(word_set):
    noun = word_set.get_random_noun()
    verb = word_set.get_random_verb()
    return f"В мире много {noun}, но лишь с тобой я могу {verb} по-настоящему."


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
            romantic_template_eight,
            romantic_template_nine,
            romantic_template_ten,
            romantic_template_eleven,
            romantic_template_twelve,
            romantic_template_thirteen,
            romantic_template_fourteen,
            romantic_template_fifteen
        ]

    def create_template(self):
        return random.choice(self.templates)

