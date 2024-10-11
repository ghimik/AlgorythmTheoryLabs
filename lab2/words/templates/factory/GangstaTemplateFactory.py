import random

from lab2.words.templates.factory.TemplateFactory import TemplateFactory


def gangsta_template_one(word_set):
    noun = word_set.get_random_noun()
    verb = word_set.get_random_verb()
    adjective = word_set.get_random_adjective()
    return f"Не тот {noun}, кто {verb}, а тот, кто {adjective}."


def gangsta_template_two(word_set):
    noun1 = word_set.get_random_noun()
    noun2 = word_set.get_random_noun()
    verb = word_set.get_random_verb()
    return f"{noun1} {verb} как {noun2}, но не каждый это видит."


def gangsta_template_three(word_set):
    verb1 = word_set.get_random_verb()
    noun = word_set.get_random_noun()
    return f"Только {verb1}, только {noun} правит улицей."


def gt4(word_set):
    noun1 = word_set.get_random_noun()
    noun2 = word_set.get_random_noun()
    verb = word_set.get_random_verb()
    return f"{noun1} {verb} как {noun2}, но не каждый это видит."


def gt5(word_set):
    verb1 = word_set.get_random_verb()
    noun = word_set.get_random_noun()
    return f"{verb1} — это не просто слово, это {noun}!"


def gt6(word_set):
    noun1 = word_set.get_random_noun()
    adjective = word_set.get_random_adjective()
    return f"{noun1} — это {adjective}, которое не забудется."


def gt7(word_set):
    verb = word_set.get_random_verb()
    noun = word_set.get_random_noun()
    return f"Если ты не {verb}, то ты не {noun}!"


def gt8(word_set):
    noun = word_set.get_random_noun()
    verb1 = word_set.get_random_verb()
    verb2 = word_set.get_random_verb()
    return f"{noun} может {verb1}, но лучше {verb2}."


def gt9(word_set):
    noun1 = word_set.get_random_noun()
    noun2 = word_set.get_random_noun()
    adjective = word_set.get_random_adjective()
    return f"{noun1} и {noun2} — это {adjective}, что разрывает шаблоны."


def gt10(word_set):
    verb = word_set.get_random_verb()
    adjective = word_set.get_random_adjective()
    return f"Жизнь — это не просто {adjective}, это умение {verb}!"


def bezumno(word_set):
    adjective = word_set.get_random_adjective()
    adjective1 = word_set.get_random_adjective()
    noun = word_set.get_random_noun()
    return f"{adjective} можно быть {adjective1}... {adjective} можно сквозь {noun}"


def gt11(word_set):
    noun = word_set.get_random_noun()
    verb = word_set.get_random_verb()
    adjective = word_set.get_random_adjective()
    return f"{adjective} {noun} всегда {verb} первым."

def gt12(word_set):
    verb1 = word_set.get_random_verb()
    verb2 = word_set.get_random_verb()
    noun = word_set.get_random_noun()
    return f"Не важно, как {verb1}, важно, что {verb2} с {noun}."

def gt13(word_set):
    noun1 = word_set.get_random_noun()
    noun2 = word_set.get_random_noun()
    return f"В жизни, как и на районе, {noun1} всегда найдёт {noun2}."

def gt14(word_set):
    verb = word_set.get_random_verb()
    noun = word_set.get_random_noun()
    adjective = word_set.get_random_adjective()
    return f"Кто {verb}, тот и {adjective} {noun}."

def gt15(word_set):
    adjective1 = word_set.get_random_adjective()
    adjective2 = word_set.get_random_adjective()
    return f"Только {adjective1} становится {adjective2} на улице."

def gt16(word_set):
    noun = word_set.get_random_noun()
    return f"Не {noun} определяет человека, а его поступки."

def gt17(word_set):
    verb1 = word_set.get_random_verb()
    verb2 = word_set.get_random_verb()
    return f"Если ты {verb1}, то {verb2} не заставит себя ждать."

def gt18(word_set):
    noun = word_set.get_random_noun()
    adjective = word_set.get_random_adjective()
    return f"Каждый {noun} должен быть {adjective}."

def gt19(word_set):
    noun1 = word_set.get_random_noun()
    noun2 = word_set.get_random_noun()
    return f"{noun1} делает {noun2}, а не наоборот."

def gt20(word_set):
    verb = word_set.get_random_verb()
    noun = word_set.get_random_noun()
    return f"Пацаны не {verb}, пацаны — {noun}."

class GangstaTemplateFactory(TemplateFactory):
    def __init__(self):
        self.templates = [
            gangsta_template_one, gangsta_template_two, gangsta_template_three,
            gt4, gt5, gt6, gt7, gt8, gt9, gt10, bezumno,
            gt11, gt12, gt13, gt14, gt15, gt16, gt17, gt18, gt19, gt20
        ]

    # override
    def create_template(self):
        return random.choice(self.templates)
