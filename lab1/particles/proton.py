from lab1.particles.base import Particle

mass_p = 1.67262171e-27
charge_p = 1.602176634e-19

class Proton(Particle):
    """Класс для протона."""
    def get_mass(self):
        return mass_p

    def get_charge(self):
        return charge_p