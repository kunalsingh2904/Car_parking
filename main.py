from car import Car
from parking import parking
from errors import FileError



input_file_name = "input.txt"

file = open(input_file_name, 'r')
first_command = file.readline().strip().split()

# Create Parking
my_parking =  parking()

if first_command[0] == "Create_parking_lot":
    print(my_parking.intialize_parking(int(first_command[1])))
else:
    raise FileError("Commands are not valid")

commands = file.readlines()
file.close()

for command in commands:
    command = command.strip().split()
    if command[0] == "Park":
        reg_num = command[1]
        driver_age = int(command[3])
        print(my_parking.add_car(Car(reg_num,driver_age)))
    elif command[0] == "Slot_numbers_for_driver_of_age":
        driver_age = int(command[1])
        print(my_parking.get_slot_number_by_driver_age(driver_age))
    elif command[0] == "Slot_number_for_car_with_number":
        reg_number = command[1]
        print(my_parking.get_car_details_by_reg_number(reg_number))
    elif command[0] == "Leave":
        slot_number = int(command[1])
        print(my_parking.remove_car(slot_number))
    elif command[0] == "Vehicle_registration_number_for_driver_of_age":
        driver_age = int(command[1])
        print(my_parking.get_slot_number_by_driver_age(driver_age))
    else:
        raise FileError("InValid Commands")
    
    


