from selectors import EpollSelector
from tires.tire import Tire

class OctoprimeTire(Tire):
    def __init__(self, wearTire):
        self.wearTire = wearTire

    def needs_service(self):
        for x in self.wearTire:
            if x >= 0.9:
                return True
            else:
                return False
