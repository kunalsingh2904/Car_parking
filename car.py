class Car:
    def __init__(self, registrations, color):
        self._reg_number = registrations
        self._driver_age = color
        
    @property
    def get_registration_number(self):
        return self._reg_number
    
    @property
    def get_driver_age(self):
        return self._driver_age