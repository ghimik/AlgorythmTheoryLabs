from lab2.phase.templates.Template import Template


class PhilosophicalTemplate(Template):
    def generate_phrase(self):
        verb1 = self.word_set.get_random_verb()
        verb2 = self.word_set.get_random_verb()
        noun = self.word_set.get_random_noun()
        return f"Лучше {verb1} и {verb2}, чем {noun} и потеря."