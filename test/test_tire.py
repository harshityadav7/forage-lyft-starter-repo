import unittest
from tires.carrigan_tire import CarriganTire
from tires.octoprime_tire import OctoprimeTire

class testOctoprimeTire(unittest.TestCase):
    def test_tire_should_be_serviced(self):
        wearTire = [0.8, 1.5, 1.3, 0.5]

        tire = OctoprimeTire(wearTire)
        self.assertTrue(tire.needs_service())

    def test_tire_should_not_be_serviced(self):
        wearTire = [0.5, 0.6, 0.3, 1]

        tire = OctoprimeTire(wearTire)
        self.assertTrue(tire.needs_service())



class testCarriganTire(unittest.TestCase):
    def test_tire_should_not_be_serviced(self):
        wearTire = [0.3, 0.5, 0.9, 0.7]
    
        tire = CarriganTire(wearTire)
        self.assertTrue(tire.needs_service())
    
    def test_tire_should_not_be_serviced(self):
        wearTire = [0.3, 0.5, 0.5, 0.8]

        tire = CarriganTire(wearTire)
        self.assertFalse(tire.needs_service())
