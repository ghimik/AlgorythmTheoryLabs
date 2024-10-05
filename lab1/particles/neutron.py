from lab1.particles.base import Particle


class Neutron(Particle):
    """Класс для нейтрона."""
    def get_mass(self):
        return 1.67492748e-27

    def get_charge(self):
        return 0