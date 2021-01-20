# parking_lot_design
Parking lot design with python code, class diagram and workflow


Parking lot Design Project

The system provides functionality of  adding, removing and listing out the (company)vehicles available at parking.

Functions description:
a). Park_vehicle - This function inserts a vehicle accordingly, also takes care of what company vehicle it is.
b). Leave_operation - This function exits a vehicle 'C' in a level 'm'.
c). Company_parked - This function allows the user to view the list of vehicles parked
for a particular company.

Functional Objects:
a). Parking_Allocation - A parking lot is made up of 'n' number of levels/floors and 'm' number of slots per floor.
b). Parking_Levels - Each level is an independent entity with a floor number, its lanes and the
slots within it. The number of lanes are designed based on the number of slots. 10 slots make one lane
c). Slots - The slots are considered as the independent entities to each other where in
the type of the vehicle is considered to fill the slot.
d). Vehicle - Object with plate no., company name and their type. A vehicle has the
attributes of license plate and the company it is from.
 

The Project contains of 2 files:
1. Parking_Lot_Design.py
2. Driver_file.py

Parking_Lot_Design.py:- 
Files performs the operation of adding, removing and listing out the vehicles.
It contains 5 classes:-
1. VehicleType: This class differenitate the type of class(car/bike).
2. Vehicle: This class defines the entities of vehicle like vehicle type(car/bike),
vehicle plate number(Registration Number), vehicle company name(Company to which vehicle belongs to).
3. Car: This class inherits the Vehicle class and signifies vehicle car.
4. Bike: This class inherits the Vehicle class and signifies vehicle bike.
5. Slots: This class defines the attributes related to slot of parking at certain level(floor) and lane, attributes
are lane (Lane of the slot), slot_num (slot Number), vehicle_type (Vehicle Type), vehicle (Vehicle Entity).
6. Parking_Levels: This Class signifies the attributes of parking level(floor), 
attributtes: floor_num(Floor number), lanes(Lanes in Floor/Level), no_of_slots(Number of slots in level).
7. Parking_Alocation: This class initializes the parking lot with providing number of floor and slots
and perform the basic designated functionality of adding, removing and listing vehicles with the linkage of other classes specified above.


Driver_file.py:- 
File test the code of Parking_Lot_Design by initalizing the Parking_Alocation class with number of floor and number of slots each floor(level has).
Perform the necessary opertion of adding, removing and listing company vehicles.
Functions defined are:
1. inserting_vehicle :- This function performs the insertion operation and uses the "Park_vehicle",
function from  Parking_Allocation class which take Vehicle entity as input ex Car(1,'Airtel').
function prompt a message "Successfuly added vehicle" after addition of each vechile.
2. removing_vehicle :- This function performs the removal operation of vehicle and uses  "Leave_operation"
function from  Parking_Allocation class which take Vehicle entity as input ex Car(1,'Airtel').
function prompt a message "Successfuly removed vehicle" after removal of vechile.
3. listing_company_vehicle :- This function outputs the list of vehicle for certain company specified.
function prints the plate number and vehicle type of all vechiles of certain given company.





