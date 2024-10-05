from lab1.particles.base import Particle


class Electron(Particle):
    """Класс для электрона."""
    def get_mass(self):
        return 9.10938356e-31

    def get_charge(self):
        return -1.602176634e-19
