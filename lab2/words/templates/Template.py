class Template:
    def __init__(self, template_function):
        self.template_function = template_function

    def generate_phrase(self, word_set):
        return self.template_function(word_set)