from lab1.particles.base import Particle

mass_n = 1.67492748e-27
charge_n = 0

class Neutron(Particle):
    """Класс для нейтрона."""
    def get_mass(self):
        return mass_n

    def get_charge(self):
        return charge_n