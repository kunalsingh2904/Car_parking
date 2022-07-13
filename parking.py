import heapq

from errors import SizeError, SlotError, CarError
from car import Car

class parking:
    def __init__(self):
        self.parking_capacity = 0
        self.available_slot = list()
        self.slot_details = dict()
        
    def intialize_parking(self, size:int):
        '''
        Initiate Parking with given size. All Slots are available to use. 
        '''
        if size > 0:
            self.parking_capacity = size
            self.available_slot = list(range(1,size+1))
            return f"Created parking of {size} slots"
        else:
            raise SizeError('Invalid parking size')
    
    def _available_slots(self):
        '''
        return minimum available slot
        '''
        if len(self.available_slot) == 0:
            return None 
        return heapq.heappop(self.available_slot)

    def add_car(self, car):
        '''
        add new car
        '''
        if car.get_registration_number and car.get_driver_age:
            slot_available = self._available_slots()
            if slot_available is None:
                raise SlotError("Sorry, Parking lot is full.")
            else:
                self.slot_details[car.get_registration_number] = (slot_available, car)
                return f'Car with vehicle registration number "{car.get_registration_number}" has been parked at slot number {slot_available}'
        raise CarError("Invalid car details")
    
    def remove_car(self,slot_number):
        '''
        remove car and free slot
        '''
        if slot_number > self.parking_capacity:
            raise SlotError("Slot Number is Not Valid.")
        if slot_number in self.available_slot:
            return "Slot already vacant"
        else:
            car_to_remove = None
            for car_detail in self.slot_details:
                if self.slot_details[car_detail][0] == slot_number:
                    car_to_remove = self.slot_details[car_detail][1]
                    break 
            if car_to_remove is not None:
                self.slot_details.pop(car_to_remove.get_registration_number)
                heapq.heappush(self.available_slot, slot_number)
            return f'Slot number {slot_number} vacated, the car with vehicle registration number "{car_to_remove.get_registration_number}" left the space, the driver of the car was of age {car_to_remove.get_driver_age}'


    def get_car_details_by_reg_number(self, reg_number):
        '''
        get car details using its registration number
        '''
        if reg_number not in self.slot_details:
            raise CarError(f"No Car found with Registration Number {reg_number}")
        else:
            slot_number = self.slot_details[reg_number][0]
            return f'{slot_number}'
        

    def get_car_reg_number_by_driver_age(self, age):
        '''
        get list of car parked by certain age driver
        '''
        car_list = list()
        for car, car_detail in self.slot_details.items():
            if car_detail[1].get_driver_age == age:
                car_list.append(car)
        return car_list

    def get_slot_number_by_driver_age(self, age):
        '''
        get list of slot where car parked by certain age driver
        '''
        slot_list = list()
        for car, car_detail in self.slot_details.items():
            if car_detail[1].get_driver_age == age:
                slot_list.append(str(car_detail[0]))
        return ",".join(slot_list)

    


