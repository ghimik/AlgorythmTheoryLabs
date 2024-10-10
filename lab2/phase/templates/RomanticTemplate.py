from lab2.phase.templates.Template import Template


class RomanticTemplate(Template):
    def generate_phrase(self):
        noun = self.word_set.get_random_noun()
        verb = self.word_set.get_random_verb()
        return f"Любовь одна, а {noun} много. Только {verb} горит в сердце."