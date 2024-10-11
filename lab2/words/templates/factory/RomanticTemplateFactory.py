import random

from lab2.words.templates.factory.TemplateFactory import TemplateFactory

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

def philosophical_template_nine(word_set):
    verb = word_set.get_random_verb()
    noun = word_set.get_random_noun()
    return f"Счастье — это {verb} {noun}."

def philosophical_template_ten(word_set):
    adjective = word_set.get_random_adjective()
    noun = word_set.get_random_noun()
    return f"{adjective.capitalize()} {noun} — это ключ к гармонии."

def philosophical_template_eleven(word_set):
    noun = word_set.get_random_noun()
    return f"Мудрость начинается с понимания {noun}."

def philosophical_template_twelve(word_set):
    verb = word_set.get_random_verb()
    return f"Изменения — это путь к {verb}."

def philosophical_template_thirteen(word_set):
    noun = word_set.get_random_noun()
    return f"Жизнь без {noun} — это просто существование."

def philosophical_template_fourteen(word_set):
    verb = word_set.get_random_verb()
    return f"Чтобы прожить жизнь в полной мере, нужно {verb}."

def philosophical_template_fifteen(word_set):
    noun = word_set.get_random_noun()
    return f"Все мы стремимся к {noun}, но забываем о {word_set.get_random_noun()}."

def philosophical_template_sixteen(word_set):
    adjective = word_set.get_random_adjective()
    return f"Наши действия — это отражение нашего {adjective} мышления."

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
            philosophical_template_eight,
            philosophical_template_nine,
            philosophical_template_ten,
            philosophical_template_eleven,
            philosophical_template_twelve,
            philosophical_template_thirteen,
            philosophical_template_fourteen,
            philosophical_template_fifteen,
            philosophical_template_sixteen
        ]

    # override
    def create_template(self):
        return random.choice(self.templates)
