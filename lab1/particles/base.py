from abc import ABC, abstractmethod

h = 6.62607015e-34  # постоянная Планка
c = 299792458  # скорость света

class Particle(ABC):
    """Базовый класс для всех частиц."""

    def __init__(self):
        self.mass = self.get_mass()
        self.charge = self.get_charge()

    @abstractmethod
    def get_mass(self):
        """Метод для получения массы частицы"""
        pass

    @abstractmethod
    def get_charge(self):
        """Метод для получения заряда частицы"""
        pass

    @property
    def specific_charge(self):
        """Расчет удельного заряда"""
        if self.mass != 0:
            return self.charge / self.mass
        return 0

    @property
    def compton_wavelength(self):
        """Расчет комптоновской длины волны на основе массы"""

        return h / (self.mass * c)

    def __str__(self):
        return f"Particle with mass {self.mass} kg and charge {self.charge} C"

    def __repr__(self):
        return f"Particle(mass={self.mass}, charge={self.charge})"

