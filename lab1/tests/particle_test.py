import pytest
from lab1.particles import Electron, Proton, Neutron, CustomParticle

def test_electron_specific_charge():
    electron = Electron()
    assert electron.specific_charge == pytest.approx(-1.75882002e11, rel=1e-6)

def test_proton_specific_charge():
    proton = Proton()
    assert proton.specific_charge == pytest.approx(9.57883315e7, rel=1e-6)

def test_neutron_specific_charge():
    neutron = Neutron()
    assert neutron.specific_charge == 0

def test_custom_particle_specific_charge():
    custom_particle = CustomParticle(2.0, 4.0)
    assert custom_particle.specific_charge == 2.0  # 4 / 2 = 2

def test_electron_compton_wavelength():
    electron = Electron()
    expected_wavelength = 2.4263102367e-12
    assert electron.compton_wavelength == pytest.approx(expected_wavelength, rel=1e-9)

def test_proton_compton_wavelength():
    proton = Proton()
    expected_wavelength = 1.32140985539e-15
    assert proton.compton_wavelength == pytest.approx(expected_wavelength, rel=1e-9)

def test_custom_particle_compton_wavelength():
    custom_particle = CustomParticle(1.0, 1.0)
    expected_wavelength = 6.62607015e-34 / (1.0 * 299792458)
    assert custom_particle.compton_wavelength == pytest.approx(expected_wavelength, rel=1e-9)

def test_particle_str():
    custom_particle = CustomParticle(2.0, 4.0)
    assert str(custom_particle) == "Custom Particle with mass 2.0 kg and charge 4.0 C"

def test_particle_repr():
    custom_particle = CustomParticle(2.0, 4.0)
    assert repr(custom_particle) == "CustomParticle(mass=2.0, charge=4.0)"

if __name__ == "__main__":
    pytest.main()
