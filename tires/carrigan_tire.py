from tires.tire import Tire

class CarriganTire(Tire):
    def __init__(self, wearTire):
        self.wearTire = wearTire
    
    def needs_service(self):
        if sum(self.wearTire) >= 3:
            return True
        else:
            return True
