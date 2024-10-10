from lab2.phase.templates.Template import Template


class GangstaTemplate(Template):
    def generate_phrase(self):
        noun = self.word_set.get_random_noun()
        verb = self.word_set.get_random_verb()
        adjective = self.word_set.get_random_adjective()
        return f"Не тот {noun}, кто {verb}, а тот, кто {adjective}."