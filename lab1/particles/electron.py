from lab1.particles.base import Particle

mass_e = 9.10938356e-31
charge_e = -1.602176634e-19

class Electron(Particle):
    """Класс для электрона."""
    def get_mass(self):
        return mass_e

    def get_charge(self):
        return charge_e
