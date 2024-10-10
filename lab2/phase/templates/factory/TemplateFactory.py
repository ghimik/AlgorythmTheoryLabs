from abc import ABC, abstractmethod


class TemplateFactory(ABC):
    @abstractmethod
    def create_template(self):
        pass
