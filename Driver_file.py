import unittest
from Parking_Lot_Design import Parking_Allocation, Car, Bike
import gc

"""
This Driver_file.py file is used for testing/building usecase for Parking_Lot_Design.py
"""
def inserting_vehicle(parkingLotObj):
    res1 = parkingLotObj.Park_vehicle(Car(1, "Incedo"))
    if res1==True:
        print("Succesfully added Vehicle")
    res2 = parkingLotObj.Park_vehicle(Car(2, "Incedo"))
    if res2==True:
        print("Succesfully added Vehicle")
    res3 = parkingLotObj.Park_vehicle(Car(3, "Genetech"))
    if res3==True:
        print("Succesfully added Vehicle")
    res4 = parkingLotObj.Park_vehicle(Car(4, "infosys"))
    if res4==True:
        print("Succesfully added Vehicle")
    res5 = parkingLotObj.Park_vehicle(Car(5, "pwc"))
    if res5==True:
        print("Succesfully added Vehicle")
    res6 = parkingLotObj.Park_vehicle(Bike(6, "Microsoft"))
    if res6==True:
        print("Succesfully added Vehicle")
    res7 = parkingLotObj.Park_vehicle(Car(7, "Google"))
    if res7==True:
        print("Succesfully added Vehicle")
    res8 = parkingLotObj.Park_vehicle(Bike(8, "Amazon"))
    if res8==True:
        print("Succesfully added Vehicle")
    res9 = parkingLotObj.Park_vehicle(Car(9, "Amazon"))
    if res9==True:
        print("Succesfully added Vehicle")
    res10 = parkingLotObj.Park_vehicle(Car(10, "Amazon"))
    if res10==True:
        print("Succesfully added Vehicle")

def removing_vehicle(parkingLotObj):
    res11 = parkingLotObj.Leave_operation(Car(10, "Amazon"))
    if res11 == True:
        print("Succesfully removed Vehicle")

def listing_company_vehicle(parkingLotObj):
    res12 = parkingLotObj.Company_parked("Amazon")
    for i in res12:
        print("Plate Number:", i.plate_num)
        print("Vehicle Type:", i.vehicle_type.name)


if __name__ == "__main__":
    # Initialize the Parking_Lot_Design Class with 3 floor and 30 slot each
    parkingLotObj = Parking_Allocation(1, 20)
    # Will perform the insertion operation in following step by inserting 10 vehicles of different companies
    inserting_vehicle(parkingLotObj)
    # Will perform the operation of leaving the vehicle from parking lot
    removing_vehicle(parkingLotObj)
    # Will list out the vehicle parked by certain company
    listing_company_vehicle(parkingLotObj)
    # garbage collection
    gc.collect()
