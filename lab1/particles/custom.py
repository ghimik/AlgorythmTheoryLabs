from lab1.particles import Particle


class CustomParticle(Particle):
    """Класс для создания пользовательской частицы."""

    def __init__(self, mass, charge):
        self._mass = mass
        self._charge = charge
        super().__init__()

    def get_mass(self):
        return self._mass

    def get_charge(self):
        return self._charge

    def __str__(self):
        return f"Custom Particle with mass {self._mass} kg and charge {self._charge} C"

    def __repr__(self):
        return f"CustomParticle(mass={self._mass}, charge={self._charge})"