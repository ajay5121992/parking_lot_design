import random
from enum import Enum


class VehicleType(Enum):
    car = 1
    bike = 2


# Vehicle class having attributes as ;
# Plate Number (Registration Number)
# Company Name (Company to which vehicle belongs to)
# Vehicle Type (car/bike)
class Vehicle:
    def __init__(self, plate_num, company_name, vehicle_type):
        self.plate_num = plate_num
        self.company_name = company_name
        self.vehicle_type = vehicle_type

    # Returns Type of Vehicle
    def get_vehicle_type(self):
        self.vehicle_type


# Class Car for Vehicle type car inherited from class vehicle
class Car(Vehicle):
    def __init__(self, plate_num, company_name):
        Vehicle.__init__(self, plate_num, company_name, VehicleType.car)


# Class Bike for Vehicle type car inherited from class vehicle
class Bike(Vehicle):
    def __init__(self, plate_num, company_name):
        Vehicle.__init__(self, plate_num, company_name, VehicleType.bike)


# Class Slot with attribute related to any slot:
# lane (Lane of the slot)
# slot_num (slot Number)
# vehicle_type (Vehicle Type)
# vehicle (Vehicle Entity)
class Slots:
    def __init__(self, lane, slot_num, vehicle_type):
        self.lane = lane
        self.slot_num = slot_num
        self.vehicle_type = vehicle_type
        self.vehicle = None

    # Check if parking is available at particular slot
    def parking_available(self):
        return self.vehicle == None

    # park a vehicle at a slot, returns True is parked successfully
    # else False
    def park_vehicle(self, vehicle):
        if self.parking_available():
            if vehicle.vehicle_type == self.vehicle_type:
                self.vehicle = vehicle
                return True
        else:
            return False

    # Removing vehicle from slot and returing the vehicle entity
    def depart_vehicle(self):
        self.vehicle = None
        return self.vehicle

    # Get type of vehicle at particular slot
    def get_vehicle(self):
        return self.vehicle

# Class Parking_Levels which signifies the attributes of parking level(floor), attributtes:
# floor_num (Floor number)
# lanes (Lanes in Floor/Level)
# no_of_slots (Number of slots in level)
class Parking_Levels:
    def __init__(self, floor_num, no_of_slots):
        self.floor_num = floor_num
        # Given in Question
        self.slots_per_lane = 10
        self.lanes = no_of_slots / self.slots_per_lane
        self.parking_slots = set()
        self.available_slots = []

        # Checking the available slots in lane
        for lane in range(int(self.lanes)):
            for slot in range(self.slots_per_lane):
                self.available_slots.append(Slots(lane, slot, random.choice(list(VehicleType))))

    # check if parking slot in available
    def parking(self,vehicle):
        for slot in self.available_slots:
            if slot.park_vehicle(vehicle):
                return True
        return False

    # Vehicle is leaving the parking
    def vehicle_leave(self, vehicle):
        for slot in self.available_slots:
            if vehicle is not None and slot.get_vehicle() is not None :
                if (slot.get_vehicle().company_name == vehicle.company_name) and (slot.get_vehicle().plate_num == vehicle.plate_num) and (slot.get_vehicle().vehicle_type.name == vehicle.vehicle_type.name) :
                    slot.depart_vehicle()
                    return True
        return False

    # get list of names of companies parked in slots
    def companies_parked(self, company_name):
        vehicles=[]
        for slot in self.available_slots:
            vehicle = slot.get_vehicle()
            if (vehicle is not None) and (vehicle.company_name == company_name):
                vehicles.append(vehicle)
        return vehicles


class Parking_Allocation:
    def __init__(self, no_of_floors, no_of_slots):
        self.levels = []
        for floor in range(no_of_floors):
            self.levels.append(Parking_Levels(floor, no_of_slots))


    # This operation inserts a vehicle.
    def Park_vehicle(self,vehicle):
        for level in self.levels:
            if level.parking(vehicle):
                return True
        return False

    # This function exits vehicle 'a`' from a level 'm'.
    def Leave_operation(self,vehicle):
        for level in self.levels:
            if level.vehicle_leave(vehicle):
                return True
        return False

    # This operation list out the vehicles for particular company
    def Company_parked(self,company_name):
        vehicle_list = []
        for level in self.levels:
            vehicle_list.extend(level.companies_parked(company_name))
        return vehicle_list