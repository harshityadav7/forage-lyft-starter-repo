from battery import Battery
from utils import add_years_to_date
class NubbinBattery(Battery):
    def __init__(self, current_date, last_service_date):
        self.current_date = current_date
        self.last_service_date = last_service_date
    
    def need_service(self):
        date_need_service = add_years_to_date(self.last_service_date, 2)
        if date_need_service < self.current_date:
            return True
        else:
            return False