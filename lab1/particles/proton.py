from lab1.particles.base import Particle


class Proton(Particle):
    """Класс для протона."""
    def get_mass(self):
        return 1.67262171e-27

    def get_charge(self):
        return 1.602176634e-19